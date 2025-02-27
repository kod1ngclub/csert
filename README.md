# csert

C assertion library

## Concept

Standard `assert()` of C language is not beautiful and not enough
for component and modular paradigm.
So, made a new assertion function for component paradigm

## Getting Started

```bash
git clone https://github.com/kod1ngclub/csert.git
cd csert

python3 make.py
# make amalgam file
# - csert.h
# - csert.c
```

## Example `csert_assert()`

```c
// ==== Assertion flags
#define FLAG_MAIN
#define FLAG_REPOSITORY_PROFILE
#define FLAG_REPOSITORY_DOCUMENT

/*
 * You can turn on or off assertion
 * by defining flags or not
 */

// ==== Assert:MAIN
#ifdef FLAG_MAIN
    #define ASSERT_MAIN(cname, cond) csert_assert(cond, #cond, cname, __FILE__, __func__, __LINE__)
#else
    #define ASSERT_MAIN(cname, cond) ((void)0)
#endif

// ==== Assert:REPOSITORY_PROFILE
#ifdef FLAG_REPOSITORY_PROFILE
    #define ASSERT_REPOSITORY_PROFILE(cname, cond) csert_assert(cond, #cond, cname, __FILE__, __func__, __LINE__)
#else
    #define ASSERT_REPOSITORY_PROFILE(cname, cond) ((void)0)
#endif

// ==== Assert:REPOSITORY_DOCUMENT
#ifdef FLAG_REPOSITORY_DOCUMENT
    #define ASSERT_REPOSITORY_DOCUMENT(cname, cond) csert_assert(cond, #cond, cname, __FILE__, __func__, __LINE__)
#else
    #define ASSERT_REPOSITORY_DOCUMENT(cname, cond) ((void)0)
#endif

// ==== Assert API
#define assertc(cname, cond) ASSERT_##cname(#cname, cond)
```

## Example `csert_assertm()`

```c
/*
 * Define flags like the previous example
 */

// ==== Assert:MAIN
#ifdef FLAG_MAIN
    #define ASSERT_MAIN(cname, message, cond) csert_assertm(message, cond, #cond, cname, __FILE__, __func__, __LINE__)
#else
    #define ASSERT_MAIN(cname, message, cond) ((void)0)
#endif

// ==== Assert:REPOSITORY_PROFILE
#ifdef FLAG_REPOSITORY_PROFILE
    #define ASSERT_REPOSITORY_PROFILE(cname, message, cond) csert_assertm(message, cond, #cond, cname, __FILE__, __func__, __LINE__)
#else
    #define ASSERT_REPOSITORY_PROFILE(cname, message, cond) ((void)0)
#endif

// ==== Assert:REPOSITORY_DOCUMENT
#ifdef FLAG_REPOSITORY_DOCUMENT
    #define ASSERT_REPOSITORY_DOCUMENT(cname, message, cond) csert_assertm(message, cond, #cond, cname, __FILE__, __func__, __LINE__)
#else
    #define ASSERT_REPOSITORY_DOCUMENT(cname, message, cond) ((void)0)
#endif

// ==== Assert API
#define assertc(cname, message, cond) ASSERT_##cname(#cname, message, cond)
```
