# Lumos App

This repository contains the Lumos frontend code.

### (Node.js, NPM) versions tested on

- (`v10.13.0`, `v6.4.1`)
- (`v12.4.0`, `v6.9.0`)

_Note: Warning from Angular CLI_- `The Angular CLI requires a minimum Node.js version of either v10.13 or v12.0.`
_Note: We do not guarantee that this system will work outside of these versions._

If you need to run different versions of Node.js in your local environment, consider installing [Node Version Manager (nvm)](https://github.com/creationix/nvm) or [Node Version Manager (nvm) for Windows](https://github.com/coreybutler/nvm-windows).

## Setup

_Relax, take a deep breath, it won't take much time._

1. Download and install Node.js:
   - **(using NVM)** see above sections for installing/using _NVM_
     - Once installed, make sure to set Node.js to the correct version for your current session!
   - **(manually)** You can download a Node.js installer for your operating system from <https://nodejs.org/en/download/>
     - Check the version of Node.js that you have installed by running `node --version` from the command line/terminal
     - Be careful of conflicting with existing installations of Node.js on your machine!
   - By installing Node.js, you also get [npm](https://www.npmjs.com/), which is a command line executable for downloading and managing Node.js packages.
2. From the command line/terminal, execute `npm install -g @angular/cli`
   - Installs [angular-cli](https://cli.angular.io/), used to run `ng-\*` commands
3. Navigate to *APP_ROOT* using `cd <APP_ROOT>`
4. `npm install`

  - Installs all dependencies and devDependencies

## Run

0. Ensure that the **server** application is running in a separate terminal.
1. Ensure that the `src/app/models/config.ts` > `DeploymentConfig.SERVER_URL` variable is correctly set to the aforementioned server's URL (e.g., http://localhost:3000).
2. If not already there, navigate to *APP_ROOT* using `cd <APP_ROOT>`
3. Execute `ng serve`
   - compiles and serves the application
4. Open the browser at <http://localhost:4200>
5. Enjoy!
6. `Ctrl-C` - stops the app

_You did well, get some rest now!_
