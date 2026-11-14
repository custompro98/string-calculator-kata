import { describe, expect, it } from "@effect/vitest";
import { Effect } from "effect";

describe("StringCalculator", () => {
  describe("add", () => {
    it.effect("is currently failing", () =>
      Effect.gen(function*() {
        expect(true).toBe(false);
      }),
    );
  });
});
