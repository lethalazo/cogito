"use client"

import { motion } from "framer-motion"
import { SectionWrapper } from "@/components/shared/section-wrapper"
import { SectionHeading } from "@/components/shared/section-heading"
import { SectionParticles } from "@/components/canvas/section-particles"

const FEATURES = [
  { feature: "Memory", cogito: "Persistent across conversations, scored and maintained", others: "Session-only or limited, platform-controlled" },
  { feature: "Data Privacy", cogito: "Client-side encrypted, wallet-derived keys", others: "Server-side storage, used for training" },
  { feature: "Authentication", cogito: "Wallet-based — anonymous, portable", others: "Email/password, centralized identity" },
  { feature: "Data Storage", cogito: "Decentralized (yours) + permanent (public)", others: "Proprietary servers" },
  { feature: "Lock-in", cogito: "None — export everything, run your own node", others: "Full platform lock-in" },
  { feature: "Open Source", cogito: "Yes (Apache 2.0)", others: "No" },
]

export function ComparisonSection() {
  return (
    <SectionWrapper id="comparison" muted>
      <SectionParticles mode="orbit" count={18} maxOpacity={0.1} />
      <SectionHeading number="04" title="VS THE REST" />

      <div className="max-w-[900px] mx-auto px-2 sm:px-0">
        <motion.p
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
          className="prose-body mb-12"
        >
          Cogito is not another chatbot wrapper.
        </motion.p>

        {/* Header row — hidden on mobile */}
        <div className="hidden md:grid grid-cols-[1fr_1.5fr_1.5fr] gap-4 mb-4 pb-3 border-b border-border">
          <span className="font-mono text-[10px] tracking-wider uppercase text-muted-foreground/60">
            Feature
          </span>
          <span className="font-mono text-[10px] tracking-wider uppercase text-accent">
            Cogito
          </span>
          <span className="font-mono text-[10px] tracking-wider uppercase text-muted-foreground/60">
            ChatGPT / Gemini / Claude
          </span>
        </div>

        <div className="space-y-0">
          {FEATURES.map((row, i) => (
            <motion.div
              key={row.feature}
              initial={{ opacity: 0, y: 15 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.4, delay: i * 0.08 }}
              className="border-b border-border/50 py-5"
            >
              {/* Desktop: grid row */}
              <div className="hidden md:grid grid-cols-[1fr_1.5fr_1.5fr] gap-4 items-start">
                <span className="font-mono text-xs tracking-wider text-foreground/70">
                  {row.feature}
                </span>
                <div className="flex items-start gap-2">
                  <span className="text-emerald-500 text-sm mt-0.5 shrink-0">✓</span>
                  <span className="text-sm text-foreground/80 leading-relaxed">
                    {row.cogito}
                  </span>
                </div>
                <div className="flex items-start gap-2">
                  <span className="text-muted-foreground/40 text-sm mt-0.5 shrink-0">✕</span>
                  <span className="text-sm text-muted-foreground leading-relaxed">
                    {row.others}
                  </span>
                </div>
              </div>

              {/* Mobile: stacked card */}
              <div className="md:hidden space-y-3">
                <span className="font-mono text-xs tracking-wider text-foreground/70 block">
                  {row.feature}
                </span>
                <div className="flex items-start gap-2 pl-2">
                  <span className="text-emerald-500 text-sm mt-0.5 shrink-0">✓</span>
                  <span className="text-sm text-foreground/80 leading-relaxed">
                    {row.cogito}
                  </span>
                </div>
                <div className="flex items-start gap-2 pl-2">
                  <span className="text-muted-foreground/40 text-sm mt-0.5 shrink-0">✕</span>
                  <span className="text-sm text-muted-foreground leading-relaxed">
                    {row.others}
                  </span>
                </div>
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </SectionWrapper>
  )
}
