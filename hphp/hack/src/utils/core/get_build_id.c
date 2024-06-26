/**
 * Copyright (c) 2014, Facebook, Inc.
 * All rights reserved.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the "hack" directory of this source tree.
 *
 */
#define CAML_NAME_SPACE
#include <caml/memory.h>
#include <caml/alloc.h>

#include <assert.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>
#include <time.h>

// from https://fburl.com/code/0l48h1h9
// where meanings are given in https://fburl.com/code/obr5oue8
extern const char* const BuildInfo_kRevision;
extern const uint64_t BuildInfo_kRevisionCommitTimeUnix;
extern const char* const BuildInfo_kBuildMode;
extern const char* const BuildInfo_kPackageName;

/**
 * Export the constants provided by Facebook's build system to ocaml-land, since
 * their FFI only allows you to call functions, not reference variables. Doing
 * it this way makes sense for Facebook internally since our build system has
 * machinery for providing these constants automatically (and no machinery
 * for doing codegen in a consistent way to build an ocaml file with them) but
 * is very roundabout for external users who have to have CMake codegen these
 * constants anyways. Sorry about that. scripts/gen_build_id.ml may help.
 */
value hh_get_build_revision(void) {
  CAMLparam0();
  CAMLlocal1(result);

  const char* const buf = BuildInfo_kRevision;
  const size_t len = strlen(buf);
  result = caml_alloc_initialized_string(len, buf);

  CAMLreturn(result);
}

value hh_get_build_package_name(void) {
  CAMLparam0();
  CAMLlocal1(result);

  const char* const buf = BuildInfo_kPackageName;
  const size_t len = strlen(buf);
  result = caml_alloc_initialized_string(len, buf);

  CAMLreturn(result);
}

static struct tm *get_built_timestamp(void) {
  unsigned long timestamp = BuildInfo_kRevisionCommitTimeUnix;
#ifdef HH_BUILD_TIMESTAMP
  if (timestamp == 0) {
    timestamp = HH_BUILD_TIMESTAMP;
  }
#endif
  // A previous version used localtime_r, which is not available on Windows
  return localtime((time_t*)&timestamp);
}

value hh_get_build_commit_time_string(void) {
  CAMLparam0();
  CAMLlocal1(result);

  char timestamp_string[25];
  struct tm *timestamp = get_built_timestamp();
  strftime(timestamp_string, sizeof(timestamp_string), "%c", timestamp);

  result = caml_copy_string(timestamp_string);
  CAMLreturn(result);
}

value hh_get_build_commit_time(void) {
  return Val_long(BuildInfo_kRevisionCommitTimeUnix);
}

value hh_get_build_mode(void) {
  CAMLparam0();
  CAMLlocal1(result);

  const size_t len = strlen(BuildInfo_kBuildMode);
  result = caml_alloc_initialized_string(len, BuildInfo_kBuildMode);

  CAMLreturn(result);
}
