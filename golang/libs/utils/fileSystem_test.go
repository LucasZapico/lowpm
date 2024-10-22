package utils

import (
	"fmt"
	"os"
	"testing"
)

// TODO: paramaterize path into test somehow

// test create directory function
func TestCreateDirectory(t *testing.T) {
	PrintInfo("------- testing create directory -------")
	path := "./bootest"
	// Create a temporary directory.

	err := CreateDirectory(path)
	if err != nil {
		PrintError("mk temp dir error", err)
		t.Error(err)
	} else {
		PrintSuccess(path + " was created successfully")
	}
	defer os.RemoveAll(path)

}

func TestDirectoryExists(t *testing.T) {
	PrintInfo("------- directory exists tests -------")
	// test directory exists	checker
	t.Run("test directory exisis truthy", func(t *testing.T) {
		PrintInfo("truthy test -- testing directory exists")
		path := "./footest"
		err := CreateDirectory(path)
		if err != nil {
			PrintError("mk temp dir error", err)
			t.Fatal(err)
		}

		exists := DirectoryExists(path)
		if exists {
			msg := fmt.Sprintf("expected directory %s exists", path)
			t.Log(msg)
		} else {
			msg := fmt.Sprintf("expected directory %s does not exists", path)
			t.Fatal(msg)
		}
		defer os.RemoveAll(path)

	})
	// test directory exists when dir is missing
	t.Run("test directory exists falsy", func(t *testing.T) {
		PrintInfo("falsy test -- testing directory does not exist")
		path := "./footest"

		exists := DirectoryExists(path)
		if exists {
			msg := fmt.Sprintf("expected directory %s exists ", path)
			t.Fatal(msg)
		} else {
			msg := fmt.Sprintf("expected directory %s not to exist", path)
			t.Log(msg)

		}
	})
}

// func TestRemoveDirectory(t *testing.T) {
// 	PrintInfo("testing remove directory")
// 	path := "./footest"
// 	// Remove the temporary directory.
// 	err := os.RemoveAll(path)
// 	if err != nil {
// 		PrintError("rm temp dir error", err)
// 		t.Error(err)
// 	} else {
// 		PrintSuccess(path + " was removed successfully")
// 	}

// }
