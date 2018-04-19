platform='unknown'
unamestr=`uname`
if [ "$unamestr" == 'Linux' ]; then
	killall chromium-browser
	while [ true ]; do python3 blog_selenium.py; sleep  $(( ( RANDOM % 100 )  + 60 )); done
else
	while [ true ]; do python blog_selenium.py; sleep  $(( ( RANDOM % 100 )  + 60 )); done
fi

