cd ~/Desktop
mkdir EnLang
cd EnLang
git clone -b main https://github.com/HttpAnimation/-EnLang.git
mv -- -EnLang main
git clone -b blank https://github.com/HttpAnimation/-EnLang.git
mv -- -EnLang blank
git clone -b gh-pages https://github.com/HttpAnimation/-EnLang.git
mv -- -EnLang gh-pages
git clone -b backend https://github.com/HttpAnimation/-EnLang.git
mv -- -EnLang backend
echo "Done"
