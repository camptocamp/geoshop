import { defineConfig } from 'vitepress'
import { withMermaid } from "vitepress-plugin-mermaid"

// https://vitepress.dev/reference/site-config
export default withMermaid(defineConfig({
  title: "Geoshop",
  description: "Getting started with Geoshop and Extract",
  base: "/geoshop/",
  mermaid: {},
  mermaidPlugin: {
    class: "mermaid",
  },
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
    ],

    sidebar: [
      {
        items: [
          { text: 'Getting started', link: '/getting-started' },
          {
            text: 'Tutorial',
            items: [
              { text: '1 - Publish a product', link: '/tutorial/1-publish-product' },
              { text: '2 - Create an user', link: '/tutorial/2-users' },
              { text: '3 - Order a product', link: '/tutorial/3-orders' },
              { text: '4 - Configure Extract', link: '/tutorial/4-extract' },
            ]
          },
          {
            text: 'Documentation',
            items: [
              { text: 'Metadatas', link: '/documentation/metadatas' },
              { text: 'Users', link: '/documentation/users' },
            ]
          },
          { text: 'Deploy', link: '/deploy' },
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/camptocamp/geoshop' }
    ],


  },
  srcExclude: [
    'README.md'
  ]
}))
