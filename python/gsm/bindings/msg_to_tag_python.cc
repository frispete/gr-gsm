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
/* BINDTOOL_HEADER_FILE(misc_utils/msg_to_tag.h)                                        */
/* BINDTOOL_HEADER_FILE_HASH(9d122cc61832a6430f5c602d697bd5b9)                     */
/***********************************************************************************/

#include <pybind11/complex.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

#include <gsm/misc_utils/msg_to_tag.h>
// pydoc.h is automatically generated in the build directory
#include <msg_to_tag_pydoc.h>

void bind_msg_to_tag(py::module& m)
{

    using msg_to_tag    = ::gr::gsm::msg_to_tag;


    py::class_<msg_to_tag, gr::sync_block, gr::block, gr::basic_block,
        std::shared_ptr<msg_to_tag>>(m, "msg_to_tag", D(msg_to_tag))

        .def(py::init(&msg_to_tag::make),
           D(msg_to_tag,make)
        )
        



        ;




}








