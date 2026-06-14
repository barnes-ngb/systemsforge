// Single source of truth for the instrument network diagram.
// Add an instrument by adding one entry to `instruments` (and any new
// systems it touches to `systems`). The diagram and any future hero
// derive from this; nothing is hand-positioned.

export interface Instrument {
  slug: string;        // page slug under /work, also the highlight key
  name: string;        // display name
  status: 'validated' | 'deployed' | 'published' | 'in-progress';
  left: string;        // system id it reaches from (smaller / more abstract)
  right: string;       // system id it reaches to (larger / more realized)
}

export interface SystemNode {
  label: string;
  scale: number;       // position on the small -> large axis, 0..1
}

// Systems are shared across instruments where the work genuinely shares them.
// That sharing is what makes the geometry chain a connected network rather
// than parallel arcs. Scale orders them small/abstract -> large/realized.
export const systems: Record<string, SystemNode> = {
  solver:        { label: 'solver',           scale: 0.08 },
  model:         { label: 'model',            scale: 0.30 },
  field:         { label: 'field',            scale: 0.58 },
  execution:     { label: 'execution',        scale: 0.80 },
  'design-intent': { label: 'design intent',  scale: 0.12 },
  construction:  { label: 'construction',     scale: 0.84 },
  problem:       { label: 'problem',          scale: 0.12 },
  knowledge:     { label: 'solved knowledge', scale: 0.72 },
  moment:        { label: 'the moment',       scale: 0.12 },
  directive:     { label: 'the directive',    scale: 0.72 },
};

export const instruments: Instrument[] = [
  { slug: 'passthrough',      name: 'passthrough',      status: 'validated',   left: 'solver',        right: 'model' },
  { slug: 'surveylink',       name: 'SurveyLink',       status: 'published',   left: 'model',         right: 'field' },
  { slug: 'directive-engine', name: 'Directive Engine', status: 'deployed',    left: 'field',         right: 'execution' },
  { slug: 'moda',             name: 'Moda',             status: 'deployed',    left: 'design-intent', right: 'construction' },
  { slug: 'strandwork',       name: 'Strandwork',       status: 'in-progress', left: 'problem',       right: 'knowledge' },
  { slug: 'compass',          name: 'Compass',          status: 'in-progress', left: 'moment',        right: 'directive' },
];
