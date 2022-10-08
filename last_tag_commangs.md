git tag | tr - \~ | sort -V | tr \~ - > tags.md
sed '/-rc/d' tags.md > tag.md
export last_tag=$(tail -n 1 tag.md)
echo "last_tag=${last_tag}"
sed -i "s!<<last_tag>>!${last_tag}!" design.kiplot.yaml