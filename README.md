# opnsense-wg-tool
python utility to autoconfigure wireguard server &amp; client instance with mullvad.

I havent written anything in python before, comments are welcome :)

## Requirements

1. Create user in opnsense with an api key.
2. Create file /etc/opnsense/config.txt with following contents.

``` 
[opnsense]
key=<opnsense_key>
secret=<opnsense_secret>
hostname=<hostname_or_ip>
[mullvad]
token=<mullvad_token
```

3. Look at mullvad_relays, pick some, call call app.add_wg_mullvad with the relay name to configure.

## To Do

1. No API for interfaces, perhaps there is a workaround. Leaving it for someone to figure out - someday. This is enough for my purposes.