#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @file
# @author (C) 2015 by Roman Khassraf <rkhassraf@gmail.com>
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

class qa_burst_sdcch_subslot_filter (gr_unittest.TestCase):
    # 102 random bursts as test input
    bursts_input = [
        '0000111100101011111011010010011001000100001001110110000110110001011011101111000100101111111000110000001111111111000111100100011111010100010011111000',
        '0001111110000000110110101010001000101000001101111100101100110010001111011010001000111100001010011101000111010111000100000111001111110011000011011000',
        '0001101110111011011011011010000001011011001011000100100110010101001111101100010100111110110011001100100011111010110111011001000111101011100001111000',
        '0000001011100110100011110111010101111000011111001011010011110000110101110010000011010110010011111001000110001111111010111011011001101010001100110000',
        '0001011001110011011101111111100110110111011101001110111110000101001111101100010100111110001111100000000110001000010000010111111011110101100000111000',
        '0001110110011011010011100010101010000100011000001111110101111101001111101100010100111110100001001101000100000001011001010110011111100010001111001000',
        '0001101100101101011110011001110110011100001100100100100110000010001111011010001000111101101101001100100001110001011001000001100000011111101000011000',
        '0000101100001011101001010001111001000000010100000111100110101000110101110010000011010110110000110010100011001111101101101001110111101001000011111000',
        '0000011011010111011111101100010100110110000001100011100001010001011011101111000100101110001110000011001100100101111000001010000101010000110101110000',
        '0000111100110111001011010100010010110100101010000000010001110010011101011000001001110100001010011111111111001010111010111010001111111101111110101000',
        '0000111101101110011111010100010100110001101110001001111100100101001111101100010100111111100010010001001100000000111010001000100011010000110111110000',
        '0000011100010011111011011001110010011000001111111110101000100000110101110010000011010111101011000100101011000011011011110000010001100110011010001000',
        '0000011011100100011101000010111010101101001111110000110001111010000111011101001000011101111110101010000011100100111101000111101110011011001001100000',
        '0000110100110111001010100011100010101001001010011001001111001001001011100001000100101111001001100100001111100111000101110111100011101100110100010000',
        '0000011101101000110111010010111001011110101000001011111000101010000111011101001000011100100100010110101110101010001000011001001110100001000101001000',
        '0000101000110000011100111010101000001101000111111101100100110010011101011000001001110101001101110101011110010100101010001110100001100010101000001000',
        '0000100010110110000111101001011000001010011110000100111101111010011101011000001001110101100010000111010100001000110001110001111101010100100101010000',
        '0000010110111011011100011101010001001011001110100011100001000101001111101100010100111110100100110001110011001011110001100000000100100111000011111000',
        '0001101110100101110101100101011101111100111010101011110001101010000111011101001000011100100010100111110110111001001000100111110111100100010010111000',
        '0000111000101011011101110110001110101111100010100000110111110010000111011101001000011101111011000101010100011111001000010000110101101110000010101000',
        '0001001010011001111011001110100001000110010111110011111001000010011101011000001001110100001101000101010010001101001010111100100101010101011100110000',
        '0000100010001111101111100100010010100000010111001011101101001000110101110010000011010110110011100111001001100101011010100101110011100001110010001000',
        '0000100100010010111100111000011000001100100001110101110011011001011011101111000100101111001011000000010111001011110011000000001101100001001000100000',
        '0001010000110010100010110111101111100100000011111000000010111010011101011000001001110101111100000011101010001010100001101000011010110000001001111000',
        '0001101101111011000010001000000010001110101111001111111111110001011011101111000100101110110001011010110110100111000000010010101110111001111011000000',
        '0001101000100010100001101100100101011100111000001101001010100010011101011000001001110100011100101100000010110101011011100111111011111101100000011000',
        '0001010110101101110000011111101100001000001001110101100000011010001111011010001000111100000100110001111110110111010101011011011100111000101111010000',
        '0000010000111000010001010010111110000100011000000101110110001000110101110010000011010111001100010011100001111101000101011110100001100010010110001000',
        '0000011110101100001001101000001010010100100111101101101000110101001111101100010100111111011001110000011000100001010011100000001100010110101001001000',
        '0001110111101011100000001011111101100110110001001100101111110010000111011101001000011101110010001111000010011110001101101111101011100001001100100000',
        '0001111110100011001100101111001001101000101110011100011000100001001011100001000100101110000110110010111111110101000110001011010110011010100011001000',
        '0001011100010110000001011011001100000101010000011010001000111111011110001001011101111001101111000011111110011001000010000011000101100011111001010000',
        '0001110111001111101101110111110000001110111011011100110110001001001011100001000100101110100101001001000110101110111110100110100100111111011001011000',
        '0001011111010100110010101100011000100011000011111000111100010101001111101100010100111111100110001110010110001110000101110000100101010111100100111000',
        '0001000100110100001010000101011001010000001111001110011010001001001011100001000100101111100011000100111100100010111001010010110100010000110000110000',
        '0001001100101001010111000101000101000000111101011111000001011010001111011010001000111100110110011000000011010000100110111101110011110011000011010000',
        '0001011010100110110011000101111111010011110001101000011100101000110101110010000011010110110100000111011101000001101010100001110111001011010101111000',
        '0000101010001100010011010101011110010101101110011110100110001010001111011010001000111100000010011011100001010001001111111100011111000011001010011000',
        '0000111001011100101100111001010101000101010111011110111101010001001011100001000100101111100010100101111011000101100000101111000101011110011111100000',
        '0000010101101111011001100001011100100101001000110111010110001111011110001001011101111000011010010010101111010000110000011001101011100000111110000000',
        '0001000001011000010001000100100111110011001101111100010011110010011101011000001001110100110100101101100011010111101110110010101101001110001101010000',
        '0000101000011101110011111001010011111001001010010000101110010001011011101111000100101111011111110000000100000110011001000100110000111001100000011000',
        '0000100101010011010110101001100100110001011010111110110100011101001111101100010100111110111000110110100011001010110011000111011111110011001011100000',
        '0001000110100001111010110101011111001000011100001111010110001001011011101111000100101111100001011001100110011001110101100001000001011011111110100000',
        '0001011010100110001000100000001110010000011000111001001110000001001011100001000100101110011011011001000111101010001010111001101100000100001101001000',
        '0000001010000101101010000000110000010101111011100110101000110111011110001001011101111001100011100100100100100000010010001111101111110011000001011000',
        '0000000111000111010110000000001001101110001001001101100110010001011011101111000100101111101011111100101001110100101000011100111001001101101011101000',
        '0000100100010111010011100110101011011010001011011011011101110010001111011010001000111100000110010111001010011100000011111100111000100100101010110000',
        '0000101111000000100110100001011000000011111111010101010011011010000111011101001000011101110010101101000100100000001100001000100111001010010000111000',
        '0000001001001101110111111011010011000011100001100011110011010001001011100001000100101110011100000010010111101100101011011111101011000000001100101000',
        '0001100111010111011000100111110000111010111001011100011111000000110101110010000011010111001000000010000010011010111001111001011011011111110101011000',
        '0000100010110111011001100110110010101011011110101001010001000001011011101111000100101111010101100010101110101111111011101000010111001111000101001000',
        '0001110000101111100101001101001111101011000000011011000101111000110101110010000011010111111100111011111000000001010111001100110100100011010000011000',
        '0000011000101001110100000000110101011101011010001101110110111001011011101111000100101111110110101011110110100111000000000011110011101000011000001000',
        '0000101001000100101010001110110111010000011011001011101010010111011110001001011101111001111010110101100100101001111000100000010001000110000000110000',
        '0000000111100101111111000110011101000110010110001110100101110001011011101111000100101110100010010011100010010001110100010101101101100111100110101000',
        '0001000011111010000000011010011001010010011111000011110111010010001111011010001000111101101110111000011010001010100111011000001000110000101000000000',
        '0001101000110010011001001110101101111110000111001101100110011001001011100001000100101110000101000111011001110001100011011101101000101001001001101000',
        '0001100111010000101101001110010001001001011000011000001011001010011101011000001001110101101110110101111101110010010010000001000100011111010100011000',
        '0001001101011001110000101110011110100001001000001111000100001001001011100001000100101110100010110100111010110010011000100111000100111111011000101000',
        '0001001101010000111101110111111011000100101011011001110001001010011101011000001001110101000000011110001101001010110001100011000110100010011010000000',
        '0000100100011000011010111010110001000101111010001001010110100001011011101111000100101111100001000101011111111110000011111111100110100100110000111000',
        '0001011101111100011001100110010001000101100001001001000010110001011011101111000100101110101100111111101111111001110110100101000011100110000001011000',
        '0001101000100100101011000001001101111011100110101010001110100010000111011101001000011101101101011111110001110001010000001111100110111101101000100000',
        '0000010101011110000000010011100010101011101111011001100111001010001111011010001000111100010001101011101000101100010110100100001101010110010111000000',
        '0001100011011000111011100010111111000000011111101010000010110001011011101111000100101111010100100110010000001010100011100001111011110010001011001000',
        '0001001011000011010010000001001110110110010101010011000101001000110101110010000011010111010010011000110011000110000101111000010100001000011111111000',
        '0000010100100110100110001010001011011000110000101011000001110001001011100001000100101111101010000111110111011010101010001100101100010100001000010000',
        '0001101100111011110100000010111000000110111101001110111110111010011101011000001001110101011110110010010011001011001110101001101010101001011000010000',
        '0001100011110111001100101110010110000110101101101111101101111001011011101111000100101111110001100010010000011100010000011011100010100111101001110000',
        '0001010011010010101001001000100111111010011101011001110110010001011011101111000100101111111010111010010001100100101100011000100110011001101101000000',
        '0000111011001001001100100100100101011111011100110101011100010010011101011000001001110101010100111100111001000001100010100111100001010011111111111000',
        '0001100101110101101110111111000100110000001111010000100001011101001111101100010100111110111111110111000010011100101001111011010100001010001010001000',
        '0000001000011111101111110000000000001100011111011010111010000111011110001001011101111001001100000001010100111111011000000110010111101001110010011000',
        '0000100000011100011111001001001000001000100010010111101011101010011101011000001001110100000000010010011001110100101111001110111111010000010001000000',
        '0001000101001011001111111101010111110010010110111111110000010001011011101111000100101111000100010000111110011101000001111100001001100100011100011000',
        '0001101101101010110000001001110111001001000001110110110000110001001011100001000100101111100001110001000000110101100001111111001001111001101101100000',
        '0000110011100000100000000010100100011001001000110010110101111001001011100001000100101110000111001100111111110011011001000001001000001111001101001000',
        '0001001111100001110110001010100011100011110011100001010100001001001011100001000100101111001000101100111101001010111000010111101000000001101100101000',
        '0000101001000010000001100001000011001010100011110111101110111001001011100001000100101110001010100101111010111000000010111011000010011001101000001000',
        '0001101000000100110100110001010111010111111001101110110101100111011110001001011101111001000110010011100100000100011101110110111010001001000111101000',
        '0000100000100110011100101001110010011011100010101101111001110010001111011010001000111101100000111011110010010111001100100010000101111111011101110000',
        '0000100111111010101000001110100011010010010010100001011010110000110101110010000011010110011000111000111111000100001010010000011011001000011100110000',
        '0001110110111100101101010011111100101100100100110001110110111001001011100001000100101110010111011011100001001010010100010101110100011111010101001000',
        '0000111001001000110010011110000010011101000001010111011011111010011101011000001001110101011101101100101110010111010001100100000011100100111101010000',
        '0001000001010011101010101011111100010010101110100001000111110010011101011000001001110101100000100101011101111101101101111000001101101010001000101000',
        '0001101000001011010011001010011010100110010100011010101101011010000111011101001000011101100010011011111111101011100110000011110110001111000101101000',
        '0000001010101101011001000000001000001001110100000111000000101001001011100001000100101110111111011101110101010011001110111111101001011010110000101000',
        '0001011110101111110100110010010110011100111010011001001110011111011110001001011101111000101010001111000111000101111000100011100010100010010100010000',
        '0001000001011110010010100001100010111111000111001111010101011111011110001001011101111001010010100101110110111111001111110010111100111010110011110000',
        '0001111100100010101100010111000000011011001111001101101001000010001111011010001000111101111000000101111001110101101001101010001110100111101011001000',
        '0000000011001001101001100111101011001011000100101100101001100010001111011010001000111101100100101001010100111000010001011000100110010101010111000000',
        '0001111000011111011100011010110000000010000000100000111000100010011101011000001001110100011101011101001001000111011101100001011010101000011011011000',
        '0001011000010101011100101011111010110101011110011011001011010010001111011010001000111100110111000110100100001100110100000001100100100111101010011000',
        '0001010101101101101001011100101001110000100101011110100011100010011101011000001001110100111100001000000111000001111100011011101000101100111100111000',
        '0000010101001010001110001001101101011011000110011011110111111000110101110010000011010110000000110010100100111001010110110011011101011001110100100000',
        '0001111111000101100000111010111010011010011110110010111000010101001111101100010100111110000110010011101101011111001000010001111111000111001111011000',
        '0000100101100011001010101100011110000111001110010010010000100001011011101111000100101110001111010000001000001101011010110101010111011011001101101000',
        '0000110000111101100001011100100011101011011000111100001000000111011110001001011101111000111000000111100100101000000101100011011001111100110011110000',
        '0000011001111001100111110110110000001111110101011110100011010010011101011000001001110101001101110111111100001001000101101101100110001111101011010000',
        '0000100001011010001010000101110000111100011110110010000010101000110101110010000011010111010001010101111111111101101100110101111010110100001110101000',
        '0000000111101000111001101101110011001100100000101111001011001111011110001001011101111001010011110001010010000011001100100001011001111010101011011000'
    ]

    # 102 sequential framenumbers
    framenumbers_input = [879852, 879853, 879854, 879855, 879856, 879857, 879858, 879859, 879860, 879861, 879862, 879863, 879864, 879865, 879866, 879867, 879868, 879869, 879870, 879871, 879872, 879873, 879874, 879875, 879876, 879877, 879878, 879879, 879880, 879881, 879882, 879883, 879884, 879885, 879886, 879887, 879888, 879889, 879890, 879891, 879892, 879893, 879894, 879895, 879896, 879897, 879898, 879899, 879900, 879901, 879902, 879903, 879904, 879905, 879906, 879907, 879908, 879909, 879910, 879911, 879912, 879913, 879914, 879915, 879916, 879917, 879918, 879919, 879920, 879921, 879922, 879923, 879924, 879925, 879926, 879927, 879928, 879929, 879930, 879931, 879932, 879933, 879934, 879935, 879936, 879937, 879938, 879939, 879940, 879941, 879942, 879943, 879944, 879945, 879946, 879947, 879948, 879949, 879950, 879951, 879952, 879953]
    
    timeslots_input = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None


    def test_001_sdcch8 (self):
        
        bursts_expected = [
            '0000011011010111011111101100010100110110000001100011100001010001011011101111000100101110001110000011001100100101111000001010000101010000110101110000',
            '0000111100110111001011010100010010110100101010000000010001110010011101011000001001110100001010011111111111001010111010111010001111111101111110101000',
            '0000111101101110011111010100010100110001101110001001111100100101001111101100010100111111100010010001001100000000111010001000100011010000110111110000',
            '0000011100010011111011011001110010011000001111111110101000100000110101110010000011010111101011000100101011000011011011110000010001100110011010001000',
            '0001000001011000010001000100100111110011001101111100010011110010011101011000001001110100110100101101100011010111101110110010101101001110001101010000',
            '0000101000011101110011111001010011111001001010010000101110010001011011101111000100101111011111110000000100000110011001000100110000111001100000011000',
            '0000100101010011010110101001100100110001011010111110110100011101001111101100010100111110111000110110100011001010110011000111011111110011001011100000',
            '0001000110100001111010110101011111001000011100001111010110001001011011101111000100101111100001011001100110011001110101100001000001011011111110100000',
            '0001001101011001110000101110011110100001001000001111000100001001001011100001000100101110100010110100111010110010011000100111000100111111011000101000',
            '0001001101010000111101110111111011000100101011011001110001001010011101011000001001110101000000011110001101001010110001100011000110100010011010000000',
            '0000100100011000011010111010110001000101111010001001010110100001011011101111000100101111100001000101011111111110000011111111100110100100110000111000',
            '0001011101111100011001100110010001000101100001001001000010110001011011101111000100101110101100111111101111111001110110100101000011100110000001011000',
        ]

        subslot = 2
        src = gsm.burst_source(self.framenumbers_input, self.timeslots_input, self.bursts_input)
        ss_filter = gsm.burst_sdcch_subslot_filter(gsm.SS_FILTER_SDCCH8, subslot)
        sink = gsm.burst_sink()

        self.tb.msg_connect(src, "out", ss_filter, "in")
        self.tb.msg_connect(ss_filter, "out", sink, "in")

        self.tb.run ()

        bursts_result = list(sink.get_burst_data())
                
        self.assertEqual(bursts_expected, bursts_result)


    def test_002_sdcch4 (self):
        
        bursts_expected = [
            '0001110111001111101101110111110000001110111011011100110110001001001011100001000100101110100101001001000110101110111110100110100100111111011001011000',
            '0001011111010100110010101100011000100011000011111000111100010101001111101100010100111111100110001110010110001110000101110000100101010111100100111000',
            '0001000100110100001010000101011001010000001111001110011010001001001011100001000100101111100011000100111100100010111001010010110100010000110000110000',
            '0001001100101001010111000101000101000000111101011111000001011010001111011010001000111100110110011000000011010000100110111101110011110011000011010000',
            '0001110110111100101101010011111100101100100100110001110110111001001011100001000100101110010111011011100001001010010100010101110100011111010101001000',
            '0000111001001000110010011110000010011101000001010111011011111010011101011000001001110101011101101100101110010111010001100100000011100100111101010000',
            '0001000001010011101010101011111100010010101110100001000111110010011101011000001001110101100000100101011101111101101101111000001101101010001000101000',
            '0001101000001011010011001010011010100110010100011010101101011010000111011101001000011101100010011011111111101011100110000011110110001111000101101000',
            '0001011000010101011100101011111010110101011110011011001011010010001111011010001000111100110111000110100100001100110100000001100100100111101010011000',
            '0001010101101101101001011100101001110000100101011110100011100010011101011000001001110100111100001000000111000001111100011011101000101100111100111000',
            '0000010101001010001110001001101101011011000110011011110111111000110101110010000011010110000000110010100100111001010110110011011101011001110100100000',
            '0001111111000101100000111010111010011010011110110010111000010101001111101100010100111110000110010011101101011111001000010001111111000111001111011000',
        ]
        
        subslot = 2
        src = gsm.burst_source(self.framenumbers_input, self.timeslots_input, self.bursts_input)
        splitter = gsm.burst_sdcch_subslot_filter(gsm.SS_FILTER_SDCCH4, subslot)
        sink = gsm.burst_sink()

        self.tb.msg_connect(src, "out", splitter, "in")
        self.tb.msg_connect(splitter, "out", sink, "in")

        self.tb.run ()

        bursts_result = list(sink.get_burst_data())
        
        self.assertEqual(bursts_result, bursts_expected)


if __name__ == '__main__':
    gr_unittest.run(qa_burst_sdcch_subslot_filter)
