#pragma once

#include <util/system/types.h>
#include <util/system/yassert.h>

namespace NPolexpr {

    enum class EVarId: ui32 {};

    class TConstId {
    public:
        constexpr TConstId(ui32 storage, ui32 idx) noexcept
            : Val{(storage << IDX_BITS) | idx}
        {
            Y_ASSERT(idx < (1 << IDX_BITS));
            Y_ASSERT(storage < (1 << STORAGE_BITS));
        }

        constexpr ui32 GetStorage() const noexcept {
            return Val >> IDX_BITS;
        }
        constexpr ui32 GetIdx() const noexcept {
            return Val & ~(~0u << IDX_BITS);
        }

        constexpr ui32 GetRepr() const noexcept {
            return Val;
        }
        constexpr static TConstId FromRepr(ui32 repr) noexcept {
            return TConstId{repr};
        }

    private:
        constexpr TConstId(ui32 repr) noexcept
            : Val{repr}
        {
        }

    public:
        constexpr static ui32 IDX_BITS = 24;
        constexpr static ui32 STORAGE_BITS = 5;

    private:
        ui32 Val;
    };

    class TFuncId {
    public:
        constexpr TFuncId(ui16 arity, ui32 idx) noexcept
            : Val{(ui32(arity) << IDX_BITS) | idx}
        {
            Y_ASSERT(idx < (1 << IDX_BITS));
            Y_ASSERT(arity < (1 << ARITY_BITS));
        }

        constexpr ui16 GetArity() const noexcept {
            return static_cast<ui16>(Val >> IDX_BITS);
        }
        constexpr ui32 GetIdx() const noexcept {
            return Val & ~(~0u << IDX_BITS);
        }

        constexpr ui32 GetRepr() const noexcept {
            return Val;
        }
        constexpr static TFuncId FromRepr(ui32 repr) noexcept {
            return TFuncId{repr};
        }

    private:
        constexpr TFuncId(ui32 repr) noexcept
            : Val{repr}
        {
        }

    private:
        constexpr static ui32 IDX_BITS = 19;
        constexpr static ui32 ARITY_BITS = 10;

    private:
        ui32 Val;
    };

}
