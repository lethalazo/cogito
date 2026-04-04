"use client"

import { motion } from "framer-motion"
import { SectionWrapper } from "@/components/shared/section-wrapper"
import { SectionHeading } from "@/components/shared/section-heading"
import { SectionParticles } from "@/components/canvas/section-particles"

const STEPS = [
  { num: "01", title: "Connect Wallet", desc: "Your wallet is your identity. Sign in with Ethereum — no passwords, no emails." },
  { num: "02", title: "Chat", desc: "The AI remembers, learns, and builds structured understanding over time." },
  { num: "03", title: "Data Stays Encrypted", desc: "Everything personal is encrypted with your wallet-derived key. Platform never sees plaintext." },
  { num: "04", title: "Knowledge Is Permanent", desc: "Shared cognition lives on permanent, public, permissionless infrastructure." },
]

export function HowItWorksSection() {
  return (
    <SectionWrapper id="how-it-works">
      <SectionParticles mode="drift" count={22} maxOpacity={0.12} />
      <SectionHeading number="03" title="HOW IT WORKS" />

      <div className="max-w-[960px] mx-auto mb-16 px-2 sm:px-0">
        <div className="flex flex-col md:flex-row items-stretch justify-between gap-4 md:gap-10">
          {STEPS.map((step, i) => (
            <div key={step.title} className="flex-1 flex items-stretch">
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.5, delay: i * 0.15 }}
                className="w-full"
              >
                <div className="text-center p-6 rounded-lg border border-border/50 bg-card/30 hover:border-accent-dim/40 hover:bg-card/60 transition-all duration-500 h-full flex flex-col justify-center">
                  <span className="font-mono text-[10px] tracking-[0.3em] text-accent-dim/50 block mb-2">
                    {step.num}
                  </span>
                  <span className="font-mono text-sm tracking-wider text-accent block mb-2">
                    {step.title}
                  </span>
                  <p className="text-sm text-muted-foreground italic leading-relaxed">
                    {step.desc}
                  </p>
                </div>
              </motion.div>
              {i < STEPS.length - 1 && (
                <span className="hidden md:flex items-center justify-center w-10 shrink-0 text-accent-dim/30 text-lg select-none">
                  →
                </span>
              )}
            </div>
          ))}
        </div>
      </div>

      <motion.div
        initial={{ opacity: 0, y: 15 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true }}
        transition={{ duration: 0.7 }}
        className="max-w-[720px] mx-auto mb-16 px-2 sm:px-0"
      >
        <p className="prose-body">
          During each conversation, Cogito follows a turn lifecycle. Before
          responding, it decrypts your memories and injects relevant context.
          After responding, it extracts new observations and learnings, encrypts
          them with your wallet key, and stores them back to decentralized storage. World
          knowledge is written to permanent storage. Plaintext only exists in memory
          during your active session.
        </p>
      </motion.div>

      <motion.div
        initial={{ opacity: 0, y: 10 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true }}
        transition={{ duration: 0.8 }}
        className="text-center"
      >
        <p className="font-serif text-2xl sm:text-3xl md:text-4xl text-foreground italic">
          &ldquo;Your wallet is the key to your cognition.&rdquo;
        </p>
      </motion.div>
    </SectionWrapper>
  )
}
