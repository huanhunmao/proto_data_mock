const vscode = require('vscode');
const path = require('path');
const { exec } = require('child_process');
const fs = require('fs');

function activate(context) {
    let disposable = vscode.commands.registerCommand('extension.generateMockData', function (uri) {
        if (!uri || !uri.fsPath) {
            vscode.window.showErrorMessage('No file selected');
            return;
        }

        const scriptDir = __dirname;
        const activeEditor = vscode.window.activeTextEditor;
        const fileName = activeEditor.document.fileName;
        const baseName = fileName.split('/').pop();

        const command = `python generate_mock_data.py ${baseName} output.json`;

        exec(command, { cwd: scriptDir }, (err, stdout, stderr) => {
            if (err) {
                vscode.window.showErrorMessage(`Error: ${stderr}`);
                return;
            }

            let jsonData;
            try {
                jsonData = JSON.parse(stdout);
            } catch (parseError) {
                vscode.window.showErrorMessage(`Error parsing JSON data: ${parseError.message}`);
                return;
            }

            const workspaceFolder = vscode.workspace.workspaceFolders[0].uri.fsPath;
            const jsonFilePath = path.join(workspaceFolder, 'mock_data.json');

            fs.writeFile(jsonFilePath, JSON.stringify(jsonData, null, 2), (err) => {
                if (err) {
                    vscode.window.showErrorMessage(`Error writing to file: ${err.message}`);
                } else {
                    vscode.window.showInformationMessage(`Data has been written to ${jsonFilePath}`);
                }
            });
        });
    });

    context.subscriptions.push(disposable);
}

function deactivate() {}

module.exports = {
    activate,
    deactivate
};
