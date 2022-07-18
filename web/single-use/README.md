# Single User

A CTFd compatible docker image for a web challenge. Scenario: The Amalgemated Single-Use Plasticware Co. has a new security system for their sales dashboard and boasts that nobody will ever get access to it. Can you prove them wrong?

## Setup

Run the included build-docker.sh script to build and deploy the container in docker.

## Solution

This scenario revolves around everything "single-use" such as time-based one-time passwords. When the user registers they are told that a four digit pin was generated for them to use for support calls but it is also used to log in, using an OTP from an app like Google Authenticator. This means that despite that code changing every thirty seconds, you can generate all 9999 possible codes and log in to any account you want by brute force. The only issue is there is a lockout function that bans you after 10 incorrect tries for 5 minutes.

The solution is to use 9 attempts trying to log in as the admin using a script that generates the codes with something like PyOTP. Then log in to your own valid account, which resets the countdown on the lockout. Then continue the brute-force process. Eventually, you can find the correct code that allows you to log in as the admin and get the flag.

See the solution video for demonstration.

