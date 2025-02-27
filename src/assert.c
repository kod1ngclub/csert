#include "../include/assert.h"

#include <stdio.h>
#include <stdlib.h>

#define CSERT_ANSI_RESET    "\033[0m"
#define CSERT_ANSI_RED      "\033[0;31m"

#define CSERT_NEWLINE       "\n"
#define CSERT_SPACE         " "

#define CSERT_HEAD          "====" CSERT_SPACE CSERT_ANSI_RED "Assertion failed!" CSERT_ANSI_RESET
#define CSERT_LINE          "|"

void csert_assert(
    const bool condition,
    const char* const expression,

    const char* const component,
    const char* const filename,
    const char* const funcname,
    const int line
) {
    // ==== pass if not debug
#ifdef NDEBUG
    return;
#endif

    // ==== pass if assertion ok
    if (condition) return;

    // ==== print embed
    printf(CSERT_NEWLINE);

    printf(CSERT_LINE CSERT_SPACE CSERT_HEAD CSERT_NEWLINE);
    printf(CSERT_LINE CSERT_NEWLINE);

    printf(CSERT_LINE CSERT_SPACE "assertion: %s" CSERT_NEWLINE, expression);
    printf(CSERT_LINE CSERT_NEWLINE);

    printf(CSERT_LINE CSERT_SPACE "- component: %s" CSERT_NEWLINE, component);
    printf(CSERT_LINE CSERT_SPACE "- filename: %s" CSERT_NEWLINE, filename);
    printf(CSERT_LINE CSERT_SPACE "- funcname: %s" CSERT_NEWLINE, funcname);
    printf(CSERT_LINE CSERT_SPACE "- line: %d" CSERT_NEWLINE, line);

    printf(CSERT_NEWLINE);
}

void csert_assertm(
    const char* const message,
    const bool condition,
    const char* const expression,

    const char* const component,
    const char* const filename,
    const char* const funcname,
    const int line
) {
    // ==== pass if not debug
#ifdef NDEBUG
    return;
#endif

    // ==== pass if assertion ok
    if (condition) return;

    // ==== print embed
    printf(CSERT_NEWLINE);

    printf(CSERT_LINE CSERT_SPACE CSERT_HEAD CSERT_NEWLINE);
    printf(CSERT_LINE CSERT_SPACE "%s" CSERT_NEWLINE, message);
    printf(CSERT_LINE CSERT_NEWLINE);

    printf(CSERT_LINE CSERT_SPACE "assertion: %s" CSERT_NEWLINE, expression);
    printf(CSERT_LINE CSERT_NEWLINE);

    printf(CSERT_LINE CSERT_SPACE "- component: %s" CSERT_NEWLINE, component);
    printf(CSERT_LINE CSERT_SPACE "- filename: %s" CSERT_NEWLINE, filename);
    printf(CSERT_LINE CSERT_SPACE "- funcname: %s" CSERT_NEWLINE, funcname);
    printf(CSERT_LINE CSERT_SPACE "- line: %d" CSERT_NEWLINE, line);

    printf(CSERT_NEWLINE);
}

#undef CSERT_ANSI_RESET
#undef CSERT_ANSI_RED
#undef CSERT_NEWLINE
#undef CSERT_SPACE
#undef CSERT_HEAD
#undef CSERT_LINE
