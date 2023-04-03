import datetime

from django.core.management.base import (BaseCommand, CommandError,
                                         no_translations)

from .scrapers.aliexpress import AliExpressScraper
from .scrapers.amazon import AmazonScraper


class Command(BaseCommand):
    help = 'Scrapes a webshop for orders using Selenium'
    requires_migrations_checks = True

    def add_arguments(self, parser):
        # Creation order is backwards to trick help-print-order
        amz = parser.add_argument_group('amazon-spesific scraper options')
        amz.add_argument(
            "-y",
            "--year",
            type=str,
            metavar="YEAR[,YEAR...]",
            help="What year(s) to get orders for. "
                    f"Default is current year ({datetime.date.today().year})."
        )
        amz.add_argument(
            "-s",
            "--start-year",
            type=int,
            help="Get all years, starting at START_YEAR."
        )

        amz.add_argument(
                '-t',
                '--tld',
                type=str.lower,
                default='de',
                help="What tld to scrape. Default `de`"
                )

        amz.add_argument(
                '--not-archived',
                action='store_true',
                help="Don't scrape archived orders."
                )

        scraper = parser.add_argument_group()
        # Apparently we do not support subparsers
        scraper.add_argument(
                'webshop',
                type=str.lower,
                choices=[
                    "aliexpress",
                    "amazon",
                    ],
                help="The online webshop to scrape orders from. (REQUIRED)"
                )

        scraper.add_argument(
                '-c',
                '--cache-orderlist',
                action='store_true',
                help="Use file for order list. Will not detect new orders with this."
                )

        # Internal hack to get command-spesific options on top
        parser._action_groups.reverse() # pylint: disable=protected-access

    @no_translations
    def handle(self, *_, **options):
        if options['webshop'] == "aliexpress":
            AliExpressScraper(self, options).command_scrape()
        elif options['webshop'] == "amazon":
            AmazonScraper(self, options).command_scrape()
        else:
            raise CommandError("Unknown webshop: {options['webshop']}")
