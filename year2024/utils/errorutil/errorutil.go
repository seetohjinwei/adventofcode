package errorutil

import "fmt"

func Assert(cond bool, messageAndArgs ...any) {
	var msg string
	if len(messageAndArgs) == 0 {
		msg = "condition failed"
	} else {
		message, isString := messageAndArgs[0].(string)
		if !isString {
			panic("message was not a string")
		}
		if len(messageAndArgs) > 1 {
			args := messageAndArgs[1:]
			msg = fmt.Sprintf(message, args)
		} else {
			msg = message
		}
	}

	if !cond {
		panic(msg)
	}
}

func AssertNil(err error) {
	if err != nil {
		panic(err)
	}
}
