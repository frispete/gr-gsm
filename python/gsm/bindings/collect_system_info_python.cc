/*
 * Copyright 2022 Free Software Foundation, Inc.
 *
 * This file is part of GNU Radio
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 *
 */

/***********************************************************************************/
/* This file is automatically generated using bindtool and can be manually edited  */
/* The following lines can be configured to regenerate this file during cmake      */
/* If manual edits are made, the following tags should be modified accordingly.    */
/* BINDTOOL_GEN_AUTOMATIC(0)                                                       */
/* BINDTOOL_USE_PYGCCXML(0)                                                        */
/* BINDTOOL_HEADER_FILE(misc_utils/collect_system_info.h)                                        */
/* BINDTOOL_HEADER_FILE_HASH(e73bdf71b433e7bcfc202a40e4399407)                     */
/***********************************************************************************/

#include <pybind11/complex.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

#include <gsm/misc_utils/collect_system_info.h>
// pydoc.h is automatically generated in the build directory
#include <collect_system_info_pydoc.h>

void bind_collect_system_info(py::module& m)
{

    using collect_system_info    = ::gr::gsm::collect_system_info;


    py::class_<collect_system_info, gr::block, gr::basic_block,
        std::shared_ptr<collect_system_info>>(m, "collect_system_info", D(collect_system_info))

        .def(py::init(&collect_system_info::make),
           D(collect_system_info,make)
        )
        




        
        .def("get_framenumbers",&collect_system_info::get_framenumbers,       
            D(collect_system_info,get_framenumbers)
        )


        
        .def("get_system_information_type",&collect_system_info::get_system_information_type,       
            D(collect_system_info,get_system_information_type)
        )


        
        .def("get_data",&collect_system_info::get_data,       
            D(collect_system_info,get_data)
        )

        ;




}








