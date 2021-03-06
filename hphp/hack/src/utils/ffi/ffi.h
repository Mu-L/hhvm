// Copyright (c) Facebook, Inc. and its affiliates.
//
// This source code is licensed under the MIT license found in the
// LICENSE file in the \"hack\" directory of this source tree.
//
// @generated SignedSource<<7c7255fa918aab88dbd426b566052d47>>


#pragma once



#include <cstdarg>
#include <cstddef>
#include <cstdint>
#include <cstdlib>
#include <ostream>
#include <new>


namespace HPHP {
namespace hackc {

/// A type to substitute for `&'a[T]`.
template<typename T>
struct Slice {
  const T *data;
  size_t len;
};

/// An alias for a type that substitutes for `&'str`.
using Str = Slice<uint8_t>;

/// Like `std::option`.
template<typename T>
struct Maybe {
  enum class Tag {
    Just,
    Nothing,
  };

  struct Just_Body {
    T _0;
  };

  Tag tag;
  union {
    Just_Body just;
  };
};


extern "C" {

void no_call_compile_only_USED_TYPES_ffi(Str, Maybe<int32_t>);

} // extern "C"

} // namespace hackc
} // namespace HPHP
