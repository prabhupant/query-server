import math
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def karl_pearson_coefficient(data1, data2):

    df1 = pd.DataFrame(data1)
    df2 = pd.DataFrame(data2)
    df = df1.append(df2, ignore_index=True)
    # print(np.corrcoef(data1, data2)[0,1])
    print(df.apply(lambda x: x.factorize()[0]).corr())
    sns.heatmap(pd.crosstab(df.title, df.link))
    plt.show()



def spearman_coefficient(data):

    df = pd.DataFrame(data, columns=['title', 'link'])

    print(df.apply(lambda x: x.factorize()[0]).corr())
    sns.heatmap(pd.crosstab(df.title, df.link))
    plt.show()


def extract_urls_to_list(data):
    lst = []
    for d in data:
        lst.append(d['link'])
    return lst

def overlap(data1, data2):

    indexes = []
    for d in data1:
        indexes.append(d)
    for d in data2:
        if d not in indexes:
            indexes.append(d)

    from itertools import combinations
    df = pd.DataFrame({"a" : data1,
                   "b" : data2},
                   index=[1,2,3,4,5,6,7,8,9,10])

    a = df.values

    d = {(i, j): np.mean(a[:, i] == a[:, j]) for i, j in combinations(range(a.shape[1]), 2)}

    res, c, vals = np.zeros((a.shape[1], a.shape[1])), \
               list(map(list, zip(*d.keys()))), list(d.values())

    res[c[0], c[1]] = vals

    res_df = pd.DataFrame(res, columns=df.columns, index=df.columns)

    print(res_df)


def overlap_second(data1, data2):
    set1 = set(data1)
    set2 = set(data2)
    count = 0
    for i in set1:
        if i in set2:
            count += 1
    percentage = (count * 100) / len(data1)
    print("Overlap percentage = {}".format(percentage))



if __name__ == '__main__':
    data1 = [
    {
        "desc": "Discover the innovative world of Apple and shop everything iPhone, iPad, Apple Watch, Mac, and Apple TV, plus explore accessories, entertainment, and expert device support.",
        "link": "https://www.apple.com/in/",
        "title": "Apple (India)"
    },
    {
        "desc": "Discover the innovative world of Apple and shop everything iPhone, iPad, Apple Watch, Mac, and Apple TV, plus explore accessories, entertainment, and expert device support.",
        "link": "https://www.apple.com/",
        "title": "Apple"
    },
    {
        "desc": "Get iPhone XR from $19.99/mo. or iPhone XS from $30.99/mo. when you trade in your iPhone online or in store. Buy now at apple.com.",
        "link": "https://www.apple.com/iphone/",
        "title": "iPhone - Apple"
    },
    {
        "desc": "Apple Computer Company was founded on April 1, 1976, by Steve Jobs, Steve Wozniak, and Ronald Wayne. The company's first product is the Apple I, a computer designed and hand-built entirely by Wozniak, and first shown to the public at the Homebrew Computer Club.",
        "link": "https://en.wikipedia.org/wiki/Apple_Inc.",
        "title": "Apple Inc. - Wikipedia"
    },
    {
        "desc": "Apple revolutionized personal technology with the introduction of the Macintosh in 1984. Today, Apple leads the world in innovation with iPhone, iPad, Mac, A...",
        "link": "https://www.youtube.com/user/Apple",
        "title": "Apple - YouTube"
    },
    {
        "desc": "Apple Card is a new kind of credit card created by Apple. And built on the principles of simplicity, transparency, and privacy.",
        "link": "https://www.apple.com/apple-card/",
        "title": "Apple Card - Apple"
    },
    {
        "desc": "iTunes is the world’s best way to play — and add to — your collection of music, movies, TV shows, apps, audiobooks, and more. Right on your Mac or PC.",
        "link": "https://www.apple.com/itunes/",
        "title": "iTunes - Apple"
    },
    {
        "desc": "The latest version of iTunes now comes installed with macOS Mojave. Upgrade today to get your favorite music, movies, TV shows, and podcasts. iTunes is also where you can join Apple Music and stream — or download and play offline — over 50 million songs, ad‑free.",
        "link": "https://www.apple.com/itunes/download/",
        "title": "iTunes - Upgrade to Get iTunes Now - Apple"
    },
    {
        "desc": "Get iPhone XR from $19.99/mo. or iPhone XS from $30.99/mo. when you trade in your iPhone online or in store. Buy now at apple.com.",
        "link": "https://www.apple.com/iphone/",
        "title": "iPhone - Apple"
    },
    {
        "desc": "iTunes is the world’s best way to play — and add to — your collection of music, movies, TV shows, apps, audiobooks, and more. Right on your Mac or PC.",
        "link": "https://www.apple.com/in/itunes/",
        "title": "iTunes - Apple (IN)"
    },
    {
        "desc": "Your Apple ID is the account you use for all Apple services.",
        "link": "https://appleid.apple.com/",
        "title": "Manage your Apple ID - Apple"
    },
    {
        "desc": "From your Apple ID account page, you can update your username, password, and payment information.",
        "link": "https://support.apple.com/en-in/apple-id",
        "title": "Apple ID - Official Apple Support"
    },
    {
        "desc": "29-03-2013 · Facebook is showing information to help you better understand the purpose of a Page. See actions taken by the people who manage and post content.",
        "link": "https://www.facebook.com/apple",
        "title": "Apple - Home | Facebook"
    },
    {
        "desc": "14.9m Followers, 6 Following, 436 Posts - See Instagram photos and videos from @apple",
        "link": "https://www.instagram.com/apple/",
        "title": "@apple • Instagram photos and videos"
    },
    {
        "desc": "Apple revolutionized personal technology with the introduction of the Macintosh in 1984. Today, Apple leads the world in innovation with iPhone, iPad, Mac, A...",
        "link": "https://www.youtube.com/channel/UCE_M8A5yxnLfW0KghEeajjw",
        "title": "Apple - YouTube"
    },
    {
        "desc": "Two thousand eighteen will be remembered as the year that Apple first achieved a market value of $1 trillion, as well as when growth in iPhones, Apple’s largest single product by far, began to slow.",
        "link": "http://fortune.com/fortune500/apple",
        "title": "Apple (AAPL) Stock Price, Financials and News | Fortune 500"
    },
    {
        "desc": "25-03-2019 · Apple TV+. The all-new streaming service featuring original stories from the most creative minds in TV and film. Learn more",
        "link": "https://www.apple.com/apple-events/march-2019/",
        "title": "Apple Events - Keynote March 2019 - Apple"
    },
    {
        "desc": "Apple Card is a new kind of credit card created by Apple. And built on the principles of simplicity, transparency, and privacy.",
        "link": "https://www.apple.com/apple-card/",
        "title": "Apple Card - Apple"
    },
    {
        "desc": "iTunes is the world’s best way to play — and add to — your collection of music, movies, TV shows, apps, audiobooks, and more. Right on your Mac or PC.",
        "link": "https://www.apple.com/in/itunes/",
        "title": "iTunes - Apple (IN)"
    },
    {
        "desc": "Apple Watch is the ultimate device for a healthy life. Choose from models including Apple Watch Series 4 with cellular and Apple Watch Series 1.",
        "link": "https://www.apple.com/in/watch/",
        "title": "Watch - Apple (IN)"
    },
    {
        "desc": "The ultimate pro notebook, MacBook Pro features faster processors, upgraded memory, the Apple T2 chip, and a Retina display with True Tone technology.",
        "link": "https://www.apple.com/in/macbook-pro/",
        "title": "MacBook Pro - Apple (IN)"
    },
    {
        "desc": "Apple revolutionized personal technology with the introduction of the Macintosh in 1984. Today, Apple leads the world in innovation with iPhone, iPad, Mac, A...",
        "link": "https://www.youtube.com/channel/UCE_M8A5yxnLfW0KghEeajjw",
        "title": "Apple - YouTube"
    },
    {
        "desc": "Gone are the days when you use complex passwords and patterns to unlock your phone, apps, and accounts. With Apple’s advanced Face ID, all you have to do is look at your phone to unlock it.",
        "link": "https://www.flipkart.com/mobiles/apple~brand/pr?sid=tyy,4io",
        "title": "Apple Mobiles - Flipkart.com"
    },
    {
        "desc": "The apple tree (Malus domestica) is a tree that grows fruit (such as apples) in the rose family best known for its juicy, tasty fruit. It is grown worldwide as a fruit tree.",
        "link": "https://simple.wikipedia.org/wiki/Apple",
        "title": "Apple - Simple English Wikipedia, the free encyclopedia"
    },
    {
        "desc": "The App Store is the best place to discover and download apps you’ll love on your iPhone, iPad, and iPod touch.",
        "link": "https://www.apple.com/ios/app-store/",
        "title": "App Store - Apple"
    },
    {
        "desc": "Apple Inc. stock price, stock quotes and financial overviews from MarketWatch.",
        "link": "https://www.marketwatch.com/investing/stock/aapl",
        "title": "Apple Inc. - MarketWatch"
    },
    {
        "desc": "Browse and download apps to your iPad, iPhone, or iPod touch from the App Store. The App Store has more than one million apps and games for your iOS device.",
        "link": "https://itunes.apple.com/US/genre/ios/id36",
        "title": "App Store Downloads on iTunes - itunes.apple.com"
    },
    {
        "desc": "View the latest movie trailers for many current and upcoming releases. Many trailers are available in high-quality HD, iPod, and iPhone versions.",
        "link": "https://trailers.apple.com/trailers/",
        "title": "iTunes Movie Trailers"
    },
    {
        "desc": "The new iMac combines power and performance with a beautiful Retina display for the ultimate all-in-one desktop experience in two sizes.",
        "link": "https://www.apple.com/in/imac/",
        "title": "iMac - Apple (IN)"
    },
    {
        "desc": "Compare features and technical specifications for all iPhone models, including iPhone XS, iPhone XR and more.",
        "link": "https://www.apple.com/in/iphone/compare/",
        "title": "iPhone - Compare Models - Apple (IN)"
    }
]
    data2 = [
    {
        "link": "https://www.apple.com/",
        "title": "Apple"
    },
    {
        "link": "https://www.marketwatch.com/investing/stock/aapl",
        "title": "AAPL Stock Price - Apple Inc. Stock Quote (U.S.: Nasdaq ..."
    },
    {
        "link": "https://en.wikipedia.org/wiki/Apple_Inc.",
        "title": "Apple Inc. - Wikipedia"
    },
    {
        "link": "https://www.nasdaq.com/symbol/aapl",
        "title": "AAPL Stock Quote - Apple Inc. Common Stock Price - Nasdaq"
    },
    {
        "link": "https://twitter.com/Apple",
        "title": "Apple (@Apple) | Twitter"
    },
    {
        "link": "https://en.wikipedia.org/wiki/History_of_Apple_Inc.",
        "title": "History of Apple Inc. - Wikipedia"
    },
    {
        "link": "https://www.imdb.com/title/tt7245840/",
        "title": "Apple (2018) - IMDb"
    },
    {
        "link": "https://appleid.apple.com/#!&page=signin",
        "title": "Manage your Apple ID"
    },
    {
        "link": "https://quotes.wsj.com/AAPL",
        "title": "AAPL Stock Price & News - Apple Inc. - Wall Street Journal"
    },
    {
        "link": "https://appleid.apple.com/us/",
        "title": "Manage your Apple ID - Apple"
    },
    {
        "link": "https://investor.apple.com/investor-relations/stock-price/",
        "title": "Apple - Stock Price"
    },
    {
        "link": "https://support.apple.com/contact",
        "title": "Contact - Official Apple Support"
    },
    {
        "link": "https://www.cnet.com/apple/",
        "title": "Apple - CNET"
    },
    {
        "link": "https://www.nasdaq.com/symbol/aapl/historical",
        "title": "Apple Inc. Common Stock (AAPL) Historical Prices & Data ..."
    },
    {
        "link": "https://jobs.apple.com/en-us/search?location=united-states-USA",
        "title": "United States - Jobs at Apple"
    },
    {
        "link": "https://markets.businessinsider.com/stocks/aapl-stock?op=1",
        "title": "AAPL Stock | APPLE Stock Price Today | Markets Insider"
    },
    {
        "link": "https://www.youtube.com/user/Apple",
        "title": "Apple - YouTube"
    },
    {
        "link": "https://finance.yahoo.com/quote/AAPL/",
        "title": "Apple Inc. (AAPL) Stock Price, Quote, History & News"
    },
    {
        "link": "https://ara.apple.com/",
        "title": "ara.apple.com - Apple Footer"
    },
    {
        "link": "https://itunes.apple.com/us/app/find-my-iphone/id376101648?mt=8",
        "title": "‎Find My iPhone on the App Store - itunes.apple.com"
    },
    {
        "link": "https://www.verizonwireless.com/support/apple/",
        "title": "Apple Support | Verizon Wireless"
    },
    {
        "link": "https://www.bestbuy.com/site/brands/apple/pcmcat128500050005.c?id=pcmcat128500050005",
        "title": "Apple Brand Store: Apple Products - Best Buy"
    },
    {
        "link": "https://www.facebook.com/apple",
        "title": "Apple - Home | Facebook"
    },
    {
        "link": "https://investor.apple.com/investor-relations/default.aspx",
        "title": "Apple - Investor Relations"
    },
    {
        "link": "https://itunes.apple.com/us/app/apple-store/id375380948",
        "title": "‎Apple Store on the App Store"
    },
    {
        "link": "https://developer.apple.com/",
        "title": "Apple Developer"
    },
    {
        "link": "https://www.instagram.com/apple/",
        "title": "@apple • Instagram photos and videos"
    },
    {
        "link": "https://www.theguardian.com/technology/apple",
        "title": "Apple | Technology | The Guardian"
    },
    {
        "link": "https://www.apple.com/",
        "title": "Apple"
    },
    {
        "link": "https://www.marketwatch.com/investing/stock/aapl",
        "title": "AAPL Stock Price - Apple Inc. Stock Quote (U.S.: Nasdaq ..."
    }
]
    karl_pearson_coefficient(data1, data2)
    #spearman_coefficient(data2)

    # extracting only URLs
    data1 = extract_urls_to_list(data1)
    data2 = extract_urls_to_list(data2)



    # spearman_coefficient(data2)
    # overlap(data1, data2)
    # data1 = [1,2,3,4,5]
    # data2 = [2,3,4,5,6,7,8,9]
    #overlap_second(data1, data2)