# Multida Server Constants
# Copyright (C) 2005 Pedram Amini <pedram.amini@gmail.com>
# Copyright (C) 2010 Jiří Suchan <yed@vanyli.net>
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
# 
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
# 
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 59 Temple
# Place, Suite 330, Boston, MA 02111-1307 USA

class server_constants:
    # IDA Sync constants
    JUMPTO      = 0x01
    NAME        = 0x02
    REG_COMMENT = 0x04
    REP_COMMENT = 0x08
    STACK_NAME  = 0x10
    
    # connection record constants
    SOCK        = 0
    MODULE      = 1
    PROJECT     = 2
    USERNAME    = 3
    TIMESTAMP   = 4

DB_HOST = 'localhost'
DB_USER = 'yed'
DB_PASS = 'heslo'
DB_NAME = 'ida'
