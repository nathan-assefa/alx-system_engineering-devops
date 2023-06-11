# Postmortem

When the new ALX DevOps project is released, I was about to make a request to the web server running on the ubuntu 14.04 container, and I was expecting a web page. However, the server returns 500 internal server Erros's. 

## Debugging Process

I had to use the command line tool called 'strace' in order to know what was causing the server to respond the 500 internal server error. Strace is a command line tool that helps devlopers to identify the system calles during the execution of a program. In addition tostrace, I have also use 'tmux' which is another command line tool that provides additional terminal whithin a single terminal. I know this sounds wired but this is what it is. What tmux does is that it provides us additional bash terminal whithin a singel terminal so that we do have to move back and forth as we do the debugging. This are the steps I followed in order to fix the apache web server. 

1. Checked running processes using `ps aux`. Two `apache2` processes - `root` and `www-data` -
were properly running.

2. Looked in the `sites-available` folder of the `/etc/apache2/` directory. Determined that
the web server was serving content located in `/var/www/html/`.

3. In one terminal, ran `strace` on the PID of the `root` Apache process. In another, curled
the server. Expected great things... only to be disappointed. `strace` gave no useful
information.

4. Repeated step 3, except on the PID of the `www-data` process. Kept expectations lower this
time... but was rewarded! `strace` revelead an `-1 ENOENT (No such file or directory)` error
occurring upon an attempt to access the file `/var/www/html/wp-includes/class-wp-locale.phpp`.

5. Looked through files in the `/var/www/html/` directory one-by-one, using Vim pattern
matching to try and locate the erroneous `.phpp` file extension. Located it in the
`wp-settings.php` file. (Line 137, `require_once( ABSPATH . WPINC . '/class-wp-locale.php' );`).

6. Removed the trailing `p` from the line.

7. Tested another `curl` on the server. 200 A-ok!

8. Wrote a Puppet manifest to automate fixing of the error.

## Summation

In short, a typo. Gotta love'em. In full, the WordPress app was encountering a critical
error in `wp-settings.php` when tyring to load the file `class-wp-locale.phpp`. The correct
file name, located in the `wp-content` directory of the application folder, was
`class-wp-locale.php`.

Patch involved a simple fix on the typo, removing the trailing `p`.

## Prevention

This outage was not a web server error, but an application error. To prevent such outages
moving forward, please keep the following in mind.

* Testing should take precedence over deploying an application before. This error would have arisen
and could have been addressed earlier if the app had been tested.

* Status monitoring. Enable some uptime-monitoring service such as
[UptimeRobot](./https://uptimerobot.com/) to alert instantly upon outage of the website.

Note that in response to this error, I wrote a Puppet manifest
[0-strace_is_your_friend.pp](https://github.com/nathan-assefa/alx-system_engineering-devops/tree/master/0x17-web_stack_debugging_3)
to automate fixing of any such identitical errors should they occur in the future. The manifest
replaces any `phpp` extensions in the file `/var/www/html/wp-settings.php` with `php`.

But of course, it will never occur again, because we're programmers, and we never make
errors! :wink:
