#
#  Copyright (c) 2011-2014 Exxeleron GmbH
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

import signal

import os
import psutil
import pwd
import subprocess

def signal_ignore():
    os.setpgrp()

def is_alive(pid):
    if pid:
        return psutil.pid_exists(pid)
    else:
        return False

def execute(cmd, bin_path, env, stdin = open(os.devnull, "r+"), stdout = None, stderr = None):
    return subprocess.Popen(cmd,
                             stdin = stdin,
                             stdout = stdout,
                             stderr = stderr,
                             cwd = bin_path,
                             env = env,
                             preexec_fn = signal_ignore
                             )

def interrupt(pid):
    if pid:
        try:
            p = psutil.Process(pid)
            p.send_signal(signal.SIGINT)
        except psutil.NoSuchProcess, e:
            raise OSError("Failed attempt to interrupt process with pid: %s.\n%s" % (pid, e))

def get_username():
    return pwd.getpwuid(os.getuid()).pw_name

def symlink(file, link):
    os.symlink(file, link)

def set_affinity(pid, cpus):
    pass

def get_affinity(pid):
    pass
