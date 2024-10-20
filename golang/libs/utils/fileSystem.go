
import (
	"os"
	"os/user"
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
func createDirectory(path string) error {
	return os.MkdirAll(path, 0755)
} 

// Function to copy a directory to the given destination path.
func copyDirectory(source, destination string) error {
	return filepath.Walk(source, func(path string, info os.FileInfo, err error) error {
			if err != nil {
					return err
			}

			destPath := filepath.Join(destination, filepath.Base(path))

			if info.IsDir() {
					// Create the directory in the destination path.
					return os.MkdirAll(destPath, info.Mode())
			} else {
					// Read the contents of the source file.
					contents, err := ioutil.ReadFile(path)
					if err != nil {
							return err
					}

					// Write the contents to the destination file.
					return ioutil.WriteFile(destPath, contents, info.Mode())
			}
	})
}