SETLOCAL ENABLEDELAYEDEXPANSION

type NUL > artwork.md
FOR /F "delims=" %%l IN (artwork.txt) DO (
    ECHO [^^![]^(%%l.adapt.crop1x1.300p.jpg^)]^(%%l^) >> artwork.md
)

type NUL > logo-mono.md
FOR /F "delims=" %%l IN (logo-mono.txt) DO (
    ECHO [^^![]^(%%l.adapt.crop1x1.100p.jpg^)]^(%%l^) >> logo-mono.md
)

type NUL > logo-color.md
FOR /F "delims=" %%l IN (logo-mono.txt) DO (
    SET string=%%l
    SET modified=!string:-mono-=-!
    ECHO [^^![]^(!modified!.adapt.crop1x1.100p.jpg^)]^(!modified!^) >> logo-color.md
)
