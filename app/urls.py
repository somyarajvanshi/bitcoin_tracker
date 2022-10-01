from flask import Blueprint
from app.bitcoin import view as bitcoin_view


blueprint = Blueprint('bp', __name__)


CRYPTO_PREFIX = '/bitcoin'
blueprint.add_url_rule(CRYPTO_PREFIX + '/price', view_func=bitcoin_view.BitcoinPrice.as_view('price'))
blueprint.add_url_rule(CRYPTO_PREFIX + '/current_price', view_func=bitcoin_view.CurrentBitcoinPrice.as_view('current_price'))
blueprint.add_url_rule(CRYPTO_PREFIX + '/pricelist/<int:page>', view_func=bitcoin_view.PriceList.as_view('list'))
blueprint.add_url_rule('/', view_func=bitcoin_view.Home.as_view('start'))