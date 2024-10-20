package utils

import (
	"fmt"

	"github.com/fatih/color"
)

func PrintError(message string, err ...error) {
	color.Set(color.FgRed)
	red := color.New(color.FgRed)
	redBold := red.Add(color.Bold).SprintFunc()
	tag := redBold("ERROR:")
	fmt.Println(tag, message, err)

}

func PrintInfo(message string) {
	cyan := color.New(color.FgCyan)
	cyanBold := cyan.Add(color.Bold).SprintFunc()
	tag := cyanBold("INFO:")
	msg := fmt.Sprintf("%s", message)
	fmt.Println(tag, msg)

}

func PrintWarning(message string) {
	yellow := color.New(color.FgYellow)
	yellowBold := yellow.Add(color.Bold).SprintFunc()
	tag := yellowBold("WARNING:")
	fmt.Println(tag, message)

}

func PrintSuccess(message string) {
	green := color.New(color.FgGreen)
	greenBold := green.Add(color.Bold).SprintFunc()
	tag := greenBold("SUCCESS:")
	fmt.Println(tag, message)
}