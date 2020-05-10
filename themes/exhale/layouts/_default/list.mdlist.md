{{ range .Pages }}
- [{{ .Title }}]({{ .RelPermalink }})
{{ end }}