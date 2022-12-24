#!/usr/bin/env python

import sys, time, re, os, signal, fcntl
from subprocess import Popen, PIPE, STDOUT
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Reloader:
    
    def __init__(self, command, delay=0, sig=signal.SIGTERM):
        self.command = command
        self.delay = delay
        self.sig = sig
        self.started = False

    def start_command(self):
        self.process = Popen(self.command, preexec_fn=os.setsid, bufsize=0, stdout=PIPE, stderr=STDOUT)
        fcntl.fcntl(self.process.stdout.fileno(), fcntl.F_SETFL, os.O_NONBLOCK)
        self.started = True

    def stop_command(self):
        if self.started:
            try:
                os.killpg(self.process.pid, self.sig)
            except OSError:
                pass
            self.started = False

    def restart_command(self):
        print("Restarting command")
        self.stop_command()
        self.start_command()

    def read(self):
        out = ''
        more = self.process != None
        while more:
            try:
                r = self.process.stdout.read()
                if not r:
                    more = False
                else:
                    out += r.decode("UTF-8")
            except IOError:
                more = False

        return out


class ReloadEventHandler(FileSystemEventHandler):

    def __init__(self, ignore_patterns=[]):
        self._modified = False
        self.ignore_patterns = [re.compile(r) for r in ignore_patterns]

    def dispatch(self, event):
        if event.is_directory:
            return

        path = os.path.basename(event.src_path)

        if any(r.match(path) for r in self.ignore_patterns):
            return

        super(ReloadEventHandler, self).dispatch(event)

    def on_modified(self, event):
        print("Detected change in " + event.src_path)
        self._modified = True

    @property
    def modified(self):
        if self._modified:
            self._modified = False
            return True
        else:
            return False


def load_ignore_patterns(name):
    patterns = []
    if os.path.exists(name):
        with open(name, "r") as f:
            pass
            for line in f:
                p = line.strip()
                if p:
                    patterns.append(p)
    return patterns


def reload(*command, ignore_patterns=[]):
    """Reload given command"""
    path = "."
    sig = signal.SIGTERM
    delay = 0.25
    ignorefile = ".reloadignore"

    ignore_patterns = ignore_patterns or load_ignore_patterns(ignorefile)

    event_handler = ReloadEventHandler(ignore_patterns)
    reloader = Reloader(command, signal)

    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    reloader.start_command()

    try:
        while True:
            time.sleep(delay)
            sys.stdout.write(reloader.read())
            sys.stdout.flush()
            if event_handler.modified:
                reloader.restart_command()
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

    reloader.stop_command()
    sys.stdout.write(reloader.read())
    sys.stdout.flush()


def reload_me(*args, ignore_patterns=[]):
    """Reload currently running command with given args"""
    
    command = [sys.executable, sys.argv[0]]
    command.extend(args)

    reload(*command, ignore_patterns=ignore_patterns)


def main():
    if len(sys.argv) < 2:
        print("Usage: reload <command>")
        exit(1)

    command = sys.argv[1:]

    reload(*command)


if __name__ == "__main__":
    main()


