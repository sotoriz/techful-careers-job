{ pkgs }: {
    deps = [
        pkgs.python39Packages.flask
        pkgs.python39Packages.pip-tools
        pkgs.sudo
        pkgs.python39Full
        pkgs.python39Packages.pip
        pkgs.cowsay
    ];
}