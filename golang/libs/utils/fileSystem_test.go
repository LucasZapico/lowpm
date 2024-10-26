package utils

import (
	"fmt"
	"os"
	"path"
	"testing"
)

// TODO: paramaterize path into test somehow

// test create directory function
func TestCreateDirectory(t *testing.T) {
	PrintInfo("------- testing create directory -------")
	path := "./gootest"
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
		PrintInfo("------ truthy test -- testing directory exists -----")
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
		PrintInfo("------- falsy test - testing directory does not exist ------")
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
	// test for copying files
	t.Run("test copy file", func(t *testing.T) {
		PrintInfo("------ truthy test - testing copy file -------")
		// remove temp dirs
		defer os.RemoveAll("./tmp")

		err := CreateDirectory("./tmp")
		if err != nil {
			PrintError("Error creating tmp dir", err)
			t.Fatal(err)
		}
		// define source and dest dirs
		sourceDir := "./tmp/foo"
		destDir := "./tmp/bar"

		// create dummy source dir
		err = CreateDirectory(sourceDir)

		if err != nil {
			PrintError("Error creating tmp/foo dir", err)
			t.Fatal(err)
		}
		// create dummy dest dir
		err = CreateDirectory(destDir)

		if err != nil {
			PrintError("Error creating tmp/bar dir", err)
			t.Fatal(err)
		}
		source := path.Join(sourceDir, "foofile.go")
		dest := path.Join(destDir, "foofile.go")

		err = os.WriteFile(source, []byte("I'm a foo file"), 0644)
		if err != nil {
			PrintError("Error writing to file", err)
			t.Fatal(err)
		}
		// copy file
		dest, err = CopyFile(source, dest)
		if err != nil {
			PrintError("copy file error", err)
			t.Fatal(err)
		} else {
			PrintSuccess(dest + " was copied successfully")
		}

	})

}
