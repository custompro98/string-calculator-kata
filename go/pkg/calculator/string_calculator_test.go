package calculator

import (
  "fmt"
  "testing"

	"github.com/stretchr/testify/assert"
)

func TestAdd(t *testing.T) {
  assert := assert.New(t)

  expected := true
  result := false

  assert.Equal(expected, result, fmt.Sprintf("expected=%v got=%v", expected, result))
}
