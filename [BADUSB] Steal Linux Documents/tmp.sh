#!/bin/sh

# Indica il percorso della cartella da verificare
directory="/home/aleff/tmp"

# Crea un elenco di tutti i file nella cartella
files=$(ls "$directory")

# Crea una cartella temporanea per i file da comprimere
tempdir=$(mktemp -d)

# Verifica i permessi di ogni file e comprime quelli che non ne richiedono
for file in $files
do
  # Verifica i permessi del file
  if [[ -r "$directory/$file" && ! -w "$directory/$file" && ! -x "$directory/$file" ]]; then
    # Copia il file nella cartella temporanea
    cp "$directory/$file" "$tempdir"
  fi
done

# Comprime i file nella cartella temporanea in un file zip
cd "$tempdir"
zip -r files.zip ./*

# Sposta il file zip nella cartella originale
mv files.zip "$directory"

# Elimina la cartella temporanea
rm -r "$tempdir"
