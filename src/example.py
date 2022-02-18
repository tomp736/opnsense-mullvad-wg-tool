import app
import warnings

# ignoring security warnings
warnings.filterwarnings('ignore')

app.add_wg_mullvad("pl1-wireguard")
app.add_wg_mullvad("pl2-wireguard")
app.add_wg_mullvad("nl1-wireguard")
app.add_wg_mullvad("nl2-wireguard")
app.add_wg_mullvad("us128-wireguard")