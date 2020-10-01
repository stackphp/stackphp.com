Stack Website All in One
========================

This repository contains (almost) everything that makes up
[stackphp.com](http://stackphp.com).

Powered by [Sculpin](http://sculpin.io). =)

### Install Composer if not exist.

`curl -s https://getcomposer.org/installer | php`

Or if you don't have curl:

`php -r "readfile('https://getcomposer.org/installer');" | php`
Build
-----

### If You Already Have Composer

`php composer.phar install`

`vendor/bin/sculpin generate --watch --server`

Your newly generated clone of [stackphp.com](http://stackphp.com) is now
accessible at `http://127.0.0.1:8080/`.



