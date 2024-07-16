hugo --contentDir collections_root --config collections.toml --destination /var/www/collections/ 
hugo --contentDir collections/lyrics --config collections.toml,collections/lyrics/lyrics.toml --destination /var/www/collections/lyrics
hugo --contentDir collections/quotes --config collections.toml,collections/quotes/quotes.toml --destination /var/www/collections/quotes
hugo --contentDir collections/comics --config collections.toml,collections/quotes/comics.toml --destination /var/www/collections/comics
