# -*- coding: utf-8 -*-
# Copyright (c) 2020 Peter Hofman <deep.core.2@gmail.com>
# Distributed under the MIT License (https://opensource.org/licenses/MIT)

import pysftp

def upload_sftp(self, full_path):

    # Debugging by setting parameters inside
    self.sftp_keyfilename = "xs4all_trigger_id_rsa"
    self.sftp_target = "shell.xs4all.nl"
    self.user_name = "trigger"

    self.sftp_key = "~/.ssh/"+self.sftp_keyfilename
    self.sftp_server = pysftp.Connection(host=self.sftp_target username=self.user_name, private_key=private_key)
    self.sftp_server.chdir(self.target_path)
    self.sftp_server.put(full_path)
    self.sftp_server.close()
