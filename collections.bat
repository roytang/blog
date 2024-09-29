hugo --contentDir collections_root --config collections.toml,local.toml --destination public
hugo --contentDir collections/lyrics --config collections.toml,local.toml,collections/lyrics/lyrics.toml --destination public/lyrics
hugo --contentDir collections/quotes --config collections.toml,local.toml,collections/quotes/quotes.toml --destination public/quotes
hugo --contentDir collections/comics --config collections.toml,local.toml,collections/comics/comics.toml --destination public/comics
hugo --contentDir collections/albums --config collections.toml,local.toml,collections/albums/albums.toml --destination public/albums
hugo --contentDir collections/stackexchange --config collections.toml,local.toml,collections/stackexchange/stackexchange.toml --destination public/stackexchange
