import click

@click.group()
def cli():
    pass

@cli.command(help="Fetch and crawl articles from a base URL.")
@click.argument('base_url', type=str, metavar='BASE_URL', required=True)
@click.argument('num', type=int, metavar='NUM', required=True)
# concurrency 参数改为必选参数
@click.option('--concurrency', type=int, required=True, show_default=True, help='Set the concurrency level for fetching and crawling.')
@click.option('--config', default='config.yaml', show_default=True, help='Path to the configuration file.')
def fetch_and_crawl(base_url, num, concurrency, config):
    asyncio.run(fetch_and_crawl(base_url, num, concurrency=concurrency, config_path=config))

if __name__ == '__main__':
    cli()