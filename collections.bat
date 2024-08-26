hugo --contentDir collections_root --config collections.toml,local.toml --destination public
hugo --contentDir collections/lyrics --config collections.toml,local.toml,collections/lyrics/lyrics.toml --destination public/lyrics
hugo --contentDir collections/quotes --config collections.toml,local.toml,collections/quotes/quotes.toml --destination public/quotes
hugo --contentDir collections/comics --config collections.toml,local.toml,collections/comics/comics.toml --destination public/comics
hugo --contentDir collections/galleries --config collections.toml,local.toml,collections/galleries/galleries.toml --destination public/galleries
