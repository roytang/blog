{{ .Site.Params.brand }} :: {{ .Site.Params.topline }}

![]({{ .Site.Params.featuredImage}})

Visit the site: ![{{.Site.BaseURL}}](.Permalink)

Latest blog posts:
{{ $pages := first 5 (where site.RegularPages "Type" "post") }}    
{{ range $pages }}
- [{{ .Title }}]({{ .Permalink }}){{ end }}

[View all posts]({{ .Permalink }}blog)

Latest shared links:
{{ $pages := first 5 (where site.RegularPages "Type" "links") }}    
{{ range $pages }}
- [{{ .Title }}]({{ .Permalink }}){{ end }}

[View all links]({{ .Permalink }}links)

Latest notes:
{{ $pages := first 5 (where site.RegularPages "Type" "notes") }}    
{{ range $pages }}
- [{{ .Date.Format .Site.Data.Formats.datetime }}]({{ .Permalink }}): {{ .Summary }}{{ end }}

[View all notes]({{ .Permalink }}notes)

Elsewhere:
{{ range ( index site.Data.Menus "elsewhere" ) }}
- [{{.Name}}]({{ .URL }}){{ end }}