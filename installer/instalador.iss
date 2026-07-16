#define MyAppName "Assistente de Risco Acadêmico"
#define MyAppVersion "1.0.0"
#define MyAppPublisher "Matheus Araújo"
#define MyAppExeName "AssistenteRiscoAcademico.exe"

[Setup]
AppId={{E08F1B22-6C83-4B37-A68D-6CF89B7E1519}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}

DefaultDirName={localappdata}\Programs\AssistenteRiscoAcademico
DefaultGroupName={#MyAppName}

OutputDir=output
OutputBaseFilename=AssistenteRiscoAcademico-Setup-v{#MyAppVersion}

Compression=lzma2
SolidCompression=yes
WizardStyle=modern

PrivilegesRequired=lowest
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible

UninstallDisplayIcon={app}\{#MyAppExeName}

[Languages]
Name: "brazilianportuguese"; MessagesFile: "compiler:Languages\BrazilianPortuguese.isl"

[Tasks]
Name: "desktopicon"; Description: "Criar um atalho na área de trabalho"; GroupDescription: "Atalhos adicionais:"; Flags: unchecked

[Files]
Source: "..\dist\AssistenteRiscoAcademico\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; WorkingDir: "{app}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; WorkingDir: "{app}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "Abrir o {#MyAppName}"; WorkingDir: "{app}"; Flags: nowait postinstall skipifsilent