String Calculator Kata
============

- Setup: `npm install`
- Run in watch mode: `npm test`
- Run once: `npm run test:run`
- Typecheck with Effect diagnostics: `npm run typecheck`

Setup automatically patches TypeScript 7 with `@effect/tsgo` to enable Effect diagnostics.

Tests use `@effect/vitest`; use `it.effect` with `Effect.gen` for Effect-based tests.

Your tests are in `src/__tests__/string_calculator.test.ts` and your function is defined in `src/string_calculator.ts`
