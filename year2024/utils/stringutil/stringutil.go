package stringutil

// Split a string by whitespace.
func SplitWhitespace(s string) []string {
	parts := make([]string, 0)

	lo := 0
	hi := 0
	for hi < len(s) {
		c := s[hi]
		if c == ' ' || c == '\n' {
			if lo != hi {
				parts = append(parts, s[lo:hi])
			}
			lo = hi + 1
		}

		hi++
	}

	if lo != hi {
		parts = append(parts, s[lo:hi])
	}

	return parts
}
