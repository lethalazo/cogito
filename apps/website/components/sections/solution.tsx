"use client"

import { motion } from "framer-motion"
import { SectionWrapper } from "@/components/shared/section-wrapper"
import { SectionHeading } from "@/components/shared/section-heading"
import { SectionParticles } from "@/components/canvas/section-particles"
import { PillarIcon } from "@/components/svg/pillar-icons"

const PILLARS = [
  {
    number: "01",
    title: "Persistent Memory",
    icon: "memory" as const,
    body: "Cogito remembers across conversations. Observations, inferences, preferences — scored by relevance, ranked by importance, maintained over time. Every interaction makes it smarter. The more you use it, the better it understands you.",
  },
  {
    number: "02",
    title: "Self-Custodial Context",
    icon: "encryption" as const,
    body: "Your data is encrypted client-side with AES-256-GCM. Encryption keys are derived from your wallet — the platform never sees plaintext. Your wallet is the key to your data. Not your keys, not your context.",
  },
  {
    number: "03",
    title: "Decentralized Infrastructure",
    icon: "decentralization" as const,
    body: "SIWE wallet authentication. User data on IPFS. World knowledge on Arweave — permanent, censorship-resistant, permissionless. No single point of failure. No platform lock-in. Run your own node if you want.",
  },
]

const containerVariants = {
  hidden: {},
  visible: { transition: { staggerChildren: 0.25 } },
}

const itemVariants = {
  hidden: { opacity: 0, y: 35 },
  visible: { opacity: 1, y: 0, transition: { duration: 0.8, ease: "easeOut" } },
}

export function SolutionSection() {
  return (
    <SectionWrapper id="solution" muted>
      <SectionParticles mode="rise" count={25} maxOpacity={0.15} />
      <SectionHeading number="02" title="THE SOLUTION" />

      <div className="max-w-[720px] mx-auto px-2 sm:px-0">
        <motion.p
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
          className="prose-body mb-16"
        >
          Cognitive AI that owns nothing — because you own everything.
        </motion.p>

        <motion.div
          variants={containerVariants}
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true, margin: "-80px" }}
          className="space-y-20"
        >
          {PILLARS.map((item, i) => (
            <motion.div key={item.title} variants={itemVariants}>
              <div className="relative">
                <span className="absolute left-0 -top-6 font-serif text-[60px] md:text-[100px] font-bold text-accent/[0.04] leading-none select-none pointer-events-none overflow-hidden">
                  {item.number}
                </span>

                <span className="section-label mb-6 block relative">
                  PILLAR {item.number}
                </span>

                <PillarIcon type={item.icon} />

                <h3 className="font-serif text-2xl md:text-3xl text-foreground mb-4">
                  {item.title}
                </h3>
                <p className="prose-body">{item.body}</p>
              </div>

              {i < PILLARS.length - 1 && (
                <motion.div
                  initial={{ scaleX: 0 }}
                  whileInView={{ scaleX: 1 }}
                  viewport={{ once: true }}
                  transition={{ duration: 0.8, delay: 0.3 }}
                  className="mt-20 flex items-center gap-4 origin-left"
                >
                  <div className="flex-1 h-px bg-border" />
                  <span className="text-accent/30 text-xs">✦</span>
                  <div className="flex-1 h-px bg-border" />
                </motion.div>
              )}
            </motion.div>
          ))}
        </motion.div>
      </div>
    </SectionWrapper>
  )
}
