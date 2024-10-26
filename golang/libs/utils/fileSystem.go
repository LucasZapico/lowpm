package utils

import (
	"errors"
	"io"
	"os"
	"os/user"
	"path/filepath"
)

// get current user
func GetCurrentUserRoot() string {
	currentUser, err := user.Current()
	if err != nil {
		panic(err)
	}

	return currentUser.HomeDir
}

// check for user level .lowpm for config
func DirectoryExists(path string) bool {
	_, err := os.Stat(path)
	if err == nil {
		return true
	} else if os.IsNotExist(err) {
		return false
	} else {
		panic(err)
	}
}

// create directory at path
func CreateDirectory(path string) error {
	return os.Mkdir(path, 0755)
}

// copyRecursive copies a directory recursively.
func CopyRecursive(source, destination string) error {
	return filepath.Walk(source, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return errors.New("failed to walk directory: " + err.Error())
		}

		// Create the destination directory if it doesn't exist.
		if info.IsDir() {
			if err := os.MkdirAll(filepath.Join(destination, filepath.Base(path)), 0755); err != nil {
				return errors.New("failed to create directory: " + err.Error())
			}
			return nil
		}

		des, err := CopyFile(path, filepath.Join(destination, filepath.Base(path)))
		PrintInfo(des)
		// Copy the file.
		if err != nil {
			return errors.New("failed to copy file: " + err.Error())
		}

		return nil
	})
}

// copyFile copies a file from source to destination.
func CopyFile(source, destination string) (string, error) {
	// Open the source file.
	srcFile, err := os.Open(source)
	if err != nil {
		return "", errors.New("failed to open source file: " + err.Error())
	}
	defer srcFile.Close()

	// Create the destination file.
	dstFile, err := os.Create(destination)
	if err != nil {
		return "", errors.New("failed to create destination file: " + err.Error())
	}
	defer dstFile.Close()

	// Copy the source file to the destination file.
	if _, err := io.Copy(dstFile, srcFile); err != nil {
		return "", errors.New("failed to copy file: " + err.Error())
	}

	return destination, nil
}
