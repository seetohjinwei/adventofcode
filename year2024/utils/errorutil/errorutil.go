package errorutil

func Assert(cond bool, message ...string) {
	if message == nil {
		message = append(message, "condition failed")
	}

	if !cond {
		panic(message)
	}
}

func AssertNil(err error) {
	if err != nil {
		panic(err)
	}
}
