"use client"

import { motion } from "framer-motion"

export function Footer() {
  return (
    <footer className="bg-background border-t border-border">
      <div className="max-w-6xl mx-auto px-6 py-16">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
          className="flex flex-col md:flex-row items-start md:items-center justify-between gap-8"
        >
          <div>
            <p className="font-serif text-xl text-foreground">Cogito</p>
            <p className="font-mono text-xs text-muted-foreground mt-2 tracking-wider">
              cogito.so
            </p>
            <a
              href="https://discontinuity.xyz"
              target="_blank"
              rel="noopener noreferrer"
              className="font-mono text-[10px] tracking-wider text-accent/50 hover:text-accent transition-colors mt-2 block"
            >
              A Discontinuity Research project &rarr;
            </a>
          </div>
          <div className="flex items-center gap-8">
            <span className="font-mono text-xs tracking-wider uppercase text-muted-foreground/30">
              GitHub
            </span>
            <span className="font-mono text-xs tracking-wider uppercase text-muted-foreground/30">
              X
            </span>
          </div>
        </motion.div>
        <motion.div
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          viewport={{ once: true }}
          transition={{ duration: 0.8, delay: 0.2 }}
          className="mt-12 pt-8 border-t border-border"
        >
          <p className="font-serif text-sm text-accent/40 italic">
            &ldquo;The AI that remembers.&rdquo;
          </p>
        </motion.div>
      </div>
    </footer>
  )
}
