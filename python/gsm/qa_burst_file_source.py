#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @file
# @author (C) 2018 by Vasil Velichkov <vvvelichkov@gmail.com>
# @section LICENSE
#
# Gr-gsm is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# Gr-gsm is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with gr-gsm; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#
#

from gnuradio import gr, gr_unittest, blocks
from gnuradio import gsm
import tempfile

class qa_burst_file_sink (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_blob_only (self):
        # prepare the input burst file
        temp = tempfile.NamedTemporaryFile()
        handle = open(temp.name, "wb")
        handle.write(bytearray([
            0x07, 0x06, 0x0a, 0x00, 0x00, 0x00, 0x00, 0xa4, 0x01, 0x00, 0x02, 0x04, 0x03, 0x01, 0x00, 0x6f,
            0xcd, 0x00, 0x00, 0x25, 0xc9, 0x82, 0x06, 0x1c, 0xf5, 0x38, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x01, 0x00, 0x01, 0x00, 0x01, 0x01, 0x01,
            0x01, 0x01, 0x01, 0x01, 0x01, 0x00, 0x01, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x01, 0x00, 0x01, 0x00, 0x01, 0x00, 0x01, 0x00, 0x01, 0x01, 0x01, 0x01, 0x00,
            0x01, 0x00, 0x01, 0x00, 0x01, 0x00, 0x01, 0x00, 0x00, 0x01, 0x00, 0x01, 0x01, 0x00, 0x01, 0x01,
            0x01, 0x00, 0x01, 0x01, 0x01, 0x01, 0x00, 0x00, 0x00, 0x01, 0x00, 0x01, 0x01, 0x00, 0x01, 0x01,
            0x01, 0x01, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x01,
            0x00, 0x01, 0x00, 0x01, 0x01, 0x01, 0x01, 0x00, 0x01, 0x00, 0x01, 0x00, 0x01, 0x00, 0x01, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x01, 0x00, 0x01, 0x00, 0x01, 0x01, 0x01,
            0x00, 0x01, 0x01, 0x01, 0x01, 0x00, 0x01, 0x00, 0x01, 0x00, 0x01, 0x00, 0x00, 0x01
            ]))
        handle.flush();
        handle.close();

        src = gsm.burst_file_source(temp.name);
        dst = gsm.burst_sink();
        self.tb.msg_connect(src, "out", dst, "in")
        self.tb.run ()

        self.assertEqual([2476418], list(dst.get_framenumbers()))
        self.assertEqual([1], list(dst.get_timeslots()))
        self.assertEqual([
            "0000001000000101010111111110101000000000010101010111101010101001011011101111000101101111100000000001010101111010101010000000010101011101111010101001"],
            list(dst.get_burst_data()))

    def test_fn_time (self):
        # prepare the input burst file
        temp = tempfile.NamedTemporaryFile()
        handle = open(temp.name, "wb")
        handle.write(bytearray([
            0x07,
            #     the additional fn_time field - 51 bytes
                  0x07, 0x07, 0x02, 0x00, 0x07, 0x66, 0x6e, 0x5f, 0x74, 0x69, 0x6d, 0x65, 0x07, 0x07, 0x0b,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x0a, 0x3b, 0x73, 0x0b, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x01, 0x07, 0x0b, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x3f, 0xe4, 0x99, 0x45,
            0xbe, 0x81, 0xc0, 0xf4,
            #     the 173 original 173 bytes
                  0x06, 0x0a, 0x00, 0x00, 0x00, 0x00, 0xa4, 0x01, 0x00, 0x02, 0x04, 0x03, 0x01, 0x00, 0x6f,
            0xcd, 0x00, 0x00, 0x25, 0xc9, 0x82, 0x06, 0x1c, 0xf5, 0x38, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x01, 0x00, 0x01, 0x00, 0x01, 0x01, 0x01,
            0x01, 0x01, 0x01, 0x01, 0x01, 0x00, 0x01, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x01, 0x00, 0x01, 0x00, 0x01, 0x00, 0x01, 0x00, 0x01, 0x01, 0x01, 0x01, 0x00,
            0x01, 0x00, 0x01, 0x00, 0x01, 0x00, 0x01, 0x00, 0x00, 0x01, 0x00, 0x01, 0x01, 0x00, 0x01, 0x01,
            0x01, 0x00, 0x01, 0x01, 0x01, 0x01, 0x00, 0x00, 0x00, 0x01, 0x00, 0x01, 0x01, 0x00, 0x01, 0x01,
            0x01, 0x01, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x01,
            0x00, 0x01, 0x00, 0x01, 0x01, 0x01, 0x01, 0x00, 0x01, 0x00, 0x01, 0x00, 0x01, 0x00, 0x01, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x01, 0x00, 0x01, 0x00, 0x01, 0x01, 0x01,
            0x00, 0x01, 0x01, 0x01, 0x01, 0x00, 0x01, 0x00, 0x01, 0x00, 0x01, 0x00, 0x00, 0x01
            ]))
        handle.flush();
        handle.close();

        src = gsm.burst_file_source(temp.name);
        dst = gsm.burst_sink();
        self.tb.msg_connect(src, "out", dst, "in")
        self.tb.run ()

        self.assertEqual([2476418], list(dst.get_framenumbers()))
        self.assertEqual([1], list(dst.get_timeslots()))
        self.assertEqual([
            "0000001000000101010111111110101000000000010101010111101010101001011011101111000101101111100000000001010101111010101010000000010101011101111010101001"],
            list(dst.get_burst_data()))

if __name__ == '__main__':
    gr_unittest.run(qa_burst_file_sink)
